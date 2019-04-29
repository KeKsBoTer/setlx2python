import keyword
import ast
import re
import codecs
from warnings import warn

from setlx2python.grammar.SetlXgrammarParser import SetlXgrammarParser
from setlx2python.grammar.SetlXgrammarLexer import SetlXgrammarLexer
from setlx2python.grammar.SetlXgrammarListener import SetlXgrammarListener
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream

from .grammar.types import *  # pylint: disable=unused-wildcard-import
from .state import TranspilerState, ClassContext


class Transpiler:
    """ A class to transpile a SetlX-AST to a Python-AST

    Takes the root element of the SetlX-AST as argument.
    The AST can be transformed with method transpile.

    Attributes
    ----------
    root : Block
        the root element of the SetlX-AST
    state : TranspilerState
        the state of the transpiler
    """

    def __init__(self, root):
        """
        Parameters
        ----------
        root : Block
            the root element of the SetlX-AST
        """
        self.root = root
        self.state = None

    def transpile(self):
        """ Translates the SetlX-AST to an equal Python-AST

        Returns the generated Python-AST
        """
        self.state = TranspilerState()

        body = self.to_python(self.root)
        imports = self.state.imports.to_python(self.state)
        return imports + body

    def to_python(self, node):
        """ Tranlates a given node / node list to a python AST

        The method calls the translation function based on the node's type and returns the result.
        The translation function of a node is the type name in lower case.

        If node is list, every element is translated and the translations are returned as a list in the same order. 
        If node is None, None is returned
        """
        if node is None:
            return None
        if isinstance(node, list):
            return [self.to_python(n) for n in node]
        else:
            name = type(node).__name__.lower()
            return getattr(self, name)(*list(node))

    def _prefix_operator(self, operation: str, expr) -> ast.Call:
        """ Turns a prefix operator into a function call

        The function translates the given expression and calls the function *operation*
        with the translated expression as argument.
        e.g. +/[1,2] -> sum([1,2])

        Parameters
        ----------
        operation : str
            The name of the function
        expr :
            The Setlx-Expression that is translated and used as argument for the function
        """
        expr = self.to_python(expr)
        return self.setlx_function(operation, [expr])

    def _binop(self, left, operator, right) -> ast.BinOp:
        """ A helper function to generate infix operations

        The function translates the left and right side of an operation
        and creates a BinOp with the given operation.
        """
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, operator, right)

    def _compare(self, left, operator, right) -> ast.Compare:
        """ A helper function to generate comparisions

        The function translates the left and right side of an operation
        and creates a Compare ast operation with the given operator.
        """
        [left, right] = self.to_python([left, right])
        return ast.Compare(left=left, ops=[operator], comparators=[right])

    def _boolop(self, left, operator, right) -> ast.BoolOp:
        """ A helper function to generate the ast for boolean operators 

        The function translates the left and right side of an operation
        and creates a BoolOp ast operation with the given operator.
        """
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.BoolOp(op=operator, values=[left, right])

    def _augassign(self, assignable, operator, right_hand_side) -> ast.AugAssign:
        """ A helper function to generate augmented assignments (e.g +=, -=) 

        The function translates the assignables and right hand side of an augmented assignment
        and creates a AugAssign ast object with the given operator.
        """
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=operator, value=rhs)

    def assignablecollectionaccess(self, assignable, exprs) -> ast.Subscript:
        """ Translates a AssignableCollectionAccess object

        A AssignableCollectionAccess is an assignment to the key of a object (e.g. a_list[2] = "test")
        It is translates to a python Subscript object, which is the corresponding python lexical element.
        e.g. a_list[2] -> a_list[2]
        """
        assignable = self.to_python(assignable)
        py_exprs = self.to_python(exprs)
        # unpack collections with only one memeber
        index = ast.List(elts=py_exprs) if len(exprs) > 1 else py_exprs[0]
        return ast.Subscript(value=assignable, slice=ast.Index(index))

    def assignableignore(self) -> ast.Name:
        """ Translates an assignment to a variable which is ignored

        In python the variable "_" is used to ignore an assignment.
        So we translate this to ast.Name(id="_").
        """
        return ast.Name(id="_")

    def assignablelist(self, assignables: list) -> ast.List:
        """ Translates an assigment to a list of variables

        A list in python ca be unpacked by writing::

            [var1, var2, var3] := a_list;

        The same is possible in python so the element is just translated
        to a list with the variables as elements.

        """
        assignables = [self.to_python(a) for a in assignables]
        return ast.List(elts=assignables)

    def assignablemember(self, assignable, member) -> ast.Attribute:
        """ Translates the assignment to the member of an object

        Attributes of objects can be assigned by writing::

            object.attribute := value;

        This notation is the same in python so it can be translated
        to an ast.Attribute object.
        """
        [target, member] = self.to_python([assignable, member])
        return ast.Attribute(value=target, attr=member)

    def assignablevariable(self, id: str):
        """ Translates a variable which is on the right hand side of an assignment

        By default this is translated to a python variable (ast.Name),
        but there are two special cases:

        1.  If the variable is called "this" we need to translate it to the corresponding keyword which is "self".

        2.  If the transpiler is in a class and the variable is a class attribute 
            the variable needs to be prefixed with "self." to enable the attribute access in pythons

        """
        if id == "this":
            return ast.Name(id="self")

        # prefix variable with "v_" if the id is a python keyword
        py_id = escape_id(id)

        if self.state.is_class_variable(py_id) and py_id not in self.state.variables and py_id not in self.state.procedures:
            return ast.Attribute(value=ast.Name(id="self"), attr=py_id)
        else:
            self.state.variables.append(py_id)

        return ast.Name(id=py_id)

    def assignment(self, assignables, right_hand_side) -> ast.Assign:
        """ Translates an assignment to a python assignment 

        If the right hand side is a single variable,
        it is wraped into a copy statement, since setlx is value based
        and this behaviour needs to be mimicked in python.
        """
        left = self.to_python(assignables)
        right = self.to_python(right_hand_side)

        if isinstance(right_hand_side, Variable):
            right = self.setlx_function("copy", [right])

        # unpack function calls (calls are not wraped in expressions in python)
        if isinstance(right, ast.Expr) and isinstance(right.value, ast.Call):
            right = right.value

        return ast.Assign(targets=left, value=right)

    def backtrack(self) -> ast.Raise:
        """ Translates a backtrack statement to a python BacktrackException raise"""
        return ast.Raise(
            exc=self.setlx_function("BacktrackException", []),
            cause=None
        )

    def block(self, stmnts: list) -> list:
        """ converts a list of setlx statements to a list of python statements

        This function converts a list of setlx statements line by line.
        """
        # copy state variables to restore them after block translation
        variables = self.state.variables[:]
        self.state.variables = []
        built_ins = self.state.built_ins[:]
        procedures = {**self.state.procedures}

        # count number of procedures in a block for non ambigous function naming
        procedure_counter = self.state.procedure_counter
        self.state.procedure_counter = 0

        py_stmnts = []
        for s in stmnts:
            level = self.state.level
            self.state.level += 1  # next depth level
            self.state.add_before = lambda stmnt: py_stmnts.append(stmnt)

            stmnt = self.to_python(s)

            self.state.add_before = None
            self.state.level = level

            # certain elements need to be warped into an expression
            if isinstance(stmnt, (ast.Compare, ast.UnaryOp, ast.BinOp, ast.Call, ast.Set, ast.SetComp)):
                stmnt = ast.Expr(value=stmnt)
            py_stmnts.append(stmnt)

        self.state.procedure_counter = procedure_counter

        self.state.variables = variables
        self.state.built_ins = built_ins
        self.state.procedures = procedures
        return py_stmnts

    def _bool_op(self, left, operator, right) -> ast.Compare:
        """ Helper function that generates a Compare element and wraps the left and right side into the bool function """
        [left_cond, right_cond] = self.to_python([left, right])
        left = call_function("bool", [left_cond])
        right = call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[operator], comparators=[right])

    def booleanequal(self, left, right) -> ast.BoolOp:
        """ x <==> y -> bool(x) == bool(y) """
        return self._bool_op(left, ast.Eq(), right)

    def booleannotequal(self, left, right) -> ast.BoolOp:
        """ x <!=> y -> bool(x) != bool(y) """
        return self._bool_op(left, ast.NotEq(), right)

    def cachedprocedure(self, params, block) -> ast.Name:
        """ See method proceduredefinition(...) """
        proc_name = f"procedure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(
            CachedProcedure(params, block), proc_name))

        return ast.Name(id=proc_name)

    def cardinality(self, expr) -> ast.Call:
        """ Python equivilant is len function 

        e.g. #A -> len(A)
        """
        expr = self.to_python(expr)
        return call_function("len", [expr])

    def cartesianproduct(self, left, right) -> ast.Call:
        """ Translated with setlx.cartesian_product function

        e.g. x >< y -> setlx.cartesian_product(x,y)
        """
        params = self.to_python([left, right])
        return self.setlx_function("cartesian_product", params)

    def check(self, check_block, backtrack_block) -> ast.Try:
        """ Check is translated to a try-catch which catches BacktrackExceptions and does nothing on exception

        e.g.::

            check{
                ...
            }

        is translated to::

            try:
                ..
            except BacktrackException: pass
        """
        body = self.to_python(check_block)
        afterBacktrack = [ast.Pass()]
        if backtrack_block != None:
            afterBacktrack = self.to_python(backtrack_block)
        return ast.Try(body=body,
                       handlers=[
                           ast.ExceptHandler(type=self.setlx_access('BacktrackException'),
                                             name=None,
                                             body=afterBacktrack)
                       ],
                       orelse=[],
                       finalbody=[])

    def classconstructor(self, id: str, params: list, block: Block, static_block: Block) -> ast.ClassDef:
        """ Creates the code for a python class based on a setlx class
        
        This class is inherits from setlx.SetlXClass.
        The class body from setlx is packed into the __init__ function of the class.
        The __init__ functions gets the parameters of the class.
        The content of the static block is translated into the class body directly.
        In the __init__ functions all static functions are converted into methods by using the function setlx.to_method(..)

        e.g.::

            class Test(x){
                this.x = x;
                static{
                    name := "Test";
                    y := procedure(a,b){
                        ...
                    };
                }
            }

        is translated to::

            class Test(setlx.SetlXClass):
                name = "Test";
                @staticmethod
                def y(a,b, self=None):
                    ...

                def __init__(self,x):
                    [x] = setlx.copy([x])
                    self.x = x
                    self.y = setlx.to_method(self,Test.y)
        """
        static_block = static_block or Block([])  # convert None to empty list

        py_id = escape_id(id)
        self.state.check_built_ins(py_id)

        self.state.class_context = ClassContext(py_id)
        self.state.class_context.variables = [escape_id(
            s.name) for s in block.stmnts+static_block.stmnts if isinstance(s, (ProcedureDefinition, LambdaDefinition))]

        for s in block.stmnts:
            if isinstance(s, Assignment):
                self.state.class_context.variables.append(
                    escape_id(s.assignables[0].id))

        procedure = Procedure(params, block)
        init = self.proceduredefinition(procedure, "__init__")
        body = init.body  # pylint: disable=no-member

        for i, s in enumerate(body):
            if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name):
                # prefix all variable assignments with self.*
                # e.g. test = 2
                #   => self.test = 2
                if isinstance(s.targets[0], ast.Name):
                    s.targets[0] = s.targets[0].id
                self.state.class_context.variables.append(s.targets[0])
                s.targets = [
                    ast.Attribute(
                        value=ast.Name(id='self'),
                        attr=s.targets[0]
                    ),
                    ast.Name(id=s.targets[0])
                ]
            # enumerate over all generated functions and assign them as class method
            # e.g. self.method = setlx.to_method(self,method)
            if isinstance(s, ast.FunctionDef):
                assign = self.to_method(s.name, False)
                self.state.class_context.variables.append(s.name)
                body.insert(i+1, assign)

        # translate static part of class
        self.state.class_context.static = True
        static = self.to_python(static_block)
        self.state.class_context.static = False

        # in setlx static functions can be called as method
        # in order to translate this properly, every static function is converted to a method in the constructor
        # looks like this: self.static_function = setlx.to_method(self,static_function)
        for s in static:
            if isinstance(s, ast.FunctionDef):
                assign = self.to_method(s.name, True)
                body.insert(0, assign)
            # check for all static lambda definitions and make them none static
            elif isinstance(s, ast.Assign) and isinstance(s.value, ast.Lambda):
                assign = self.to_method(s.targets[0].id, True)
                body.insert(0, assign)

        self.state.class_context = None
        return ast.ClassDef(
            name=py_id,
            bases=[self.setlx_access("SetlXClass")],
            keywords=[],
            body=static+[init],
            decorator_list=[]
        )

    def closure(self, params, block) -> ast.Name:
        """ Closures are translated like normal procedures (see procedure(..))"""
        warn("closures are translated as normal python functions, so they can only read from variables outside the scope")
        proc_name = f"closure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(
            Closure(params, block), proc_name))

        return ast.Name(id=proc_name)

    def collectionaccess(self, params, callable) -> ast.Subscript:
        """ Tranalated to Python Subscript 

        Three possible params described by the following examples:
        e.g.    collection[1] -> collection[1]
                collection[1,2] -> collection[[1,2]]
                collection[1..2] -> collection[1:2]
        """
        py_callable = self.to_python(callable)

        if isinstance(params, list):
            py_params = ast.List(elts=self.to_python(params))
        else:
            py_params = self.to_python(params)

        if isinstance(params, ListRange):
            return ast.Subscript(value=py_callable, slice=py_params)
        else:
            index = ast.Index(value=py_params)
            return ast.Subscript(value=py_callable, slice=index)

    def collectmap(self, expr, callable) -> ast.Call:
        """ Translated by calling the method "collect" on the object 

        e.g. collection{1} -> collection.collect(1)
        """
        [py_var, py_expr] = self.to_python([callable, expr])
        return ast.Call(func=ast.Attribute(value=py_var, attr='collect'), args=[py_expr], keywords=[])

    def condition(self, expression):
        """ Translated by translating the cxondition's expression """
        return self.to_python(expression)

    def conjunction(self, left, right) -> ast.BoolOp:
        """ Same in SetlX and Python (and, &&) """
        return self._boolop(left, ast.And(), right)

    def difference(self, left, right) -> ast.BinOp:
        """ Same in SetlX and Python (-) """
        return self._binop(left, ast.Sub(), right)

    def differenceassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ Same in SetlX and Python (-=) """
        return self._augassign(assignable, ast.Sub(), right_hand_side)

    def disjunction(self, left, right) -> ast.BoolOp:
        """ Same in SetlX and Python (or, ||) """
        return self._boolop(left, ast.Or(), right)

    def dowhile(self, condition, block) -> ast.While:
        """ Translated by converting to Python while structure with condition at end

        e.g.::

            do{
                ...
            }while(x > 10);

        is transalted to::

            while True:
                ...
                if not(x > 10):
                    break
        """
        [py_condition, py_block] = self.to_python([condition, block])
        break_block = [ast.Break()]
        negate = ast.UnaryOp(op=ast.Not(), operand=py_condition)
        if_break = ast.If(test=negate, body=break_block, orelse=[])
        py_block.append(if_break)
        return ast.While(test=bool_true(), body=py_block, orelse=[])

    def equal(self, left, right) -> ast.Compare:
        """ Same in SetlX and Python (==)"""
        return self._compare(left, ast.Eq(), right)

    def exists(self, iter_chain, condition) -> ast.Call:
        """ Translated with Python's any function 

        e.g. exists(x in y | x > 2) -> any(x > 2 for x in y)
        """
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        expr = expr.args[0]  # unpack list from setlx.List object
        return call_function("any", [ast.GeneratorExp(elt=expr.elt, generators=expr.generators)])

    def exit(self):
        """ Translated by calling python's exit function"""
        return call_function("exit", [])

    def explicitlist(self, exprs) -> ast.Call:
        """ Translated by using custom setlx.List 

        e.g. [1,2,3] -> seltx.List([1,2,3])
        """
        list_arg = ast.List(elts=self.to_python(exprs))
        return self.setlx_function("List", [list_arg])

    def explicitlistwithrest(self, exprs, rest) -> ast.Call:
        """ Translated by adding the rest as starred element to the list

        e.g. [1,2|x] -> setlx.List([1,2,*x])
        """
        py_exprs = self.to_python(exprs)
        py_exprs.append(ast.Starred(
            value=self.to_python(rest)
        ))
        elts = ast.List(elts=py_exprs)
        return self.setlx_function("List", [elts])

    def factorial(self, expr) -> ast.Call:
        """ Translated by using the setlx.factorial function 

        e.g. 5! -> setlx.factorial(5)
        """
        expr = self.to_python(expr)
        return self.setlx_function("factorial", [expr])

    def forall(self, iter_chain, condition) -> ast.Call:
        """ Translated with Python all function 

        e.g. forall(x in y | x > 2) -> all(x > 2 for x in y)
        """
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        expr = expr.args[0]  # unpack list from setlx.List object
        return call_function("all", [ast.GeneratorExp(elt=expr.elt, generators=expr.generators)])

    def functioncall(self, params, callable) -> ast.Call:
        """ Function calls in SetlX and Python are the same so they are translated equally 

        There two speciall functions:
        1. "load" is translated to a import statement (load("test.stlx") -> from test import *)
        2. "eval" gets the global and local variables as extra parameters (eval(x) -> setlx.eval(x,globals(),locals()))
        """
        py_params = self.to_python(params)

        if isinstance(callable, Variable):
            if callable.id == "load":
                return import_call(py_params[0].s)
            elif callable.id == "eval":
                return self.setlx_function("eval", [py_params[0],
                                                    ast.Call(func=ast.Name(id='globals'),
                                                             args=[], keywords=[]),
                                                    ast.Call(func=ast.Name(id='locals'), args=[], keywords=[])])

        expr = self.to_python(callable)
        return ast.Call(expr, py_params, [])

    def greaterorequal(self, left, right) -> ast.Compare:
        """ same in SetlX and Python (>=) """
        return self._compare(left, ast.GtE(), right)

    def greaterthan(self, left, right) -> ast.Compare:
        """ same in SetlX and Python (>) """
        return self._compare(left, ast.Gt(), right)

    def ifthen(self, condition, block, else_list) -> ast.If:
        """ Translated to a Python If statement, which has the same structure as in SetlX """
        [condition, block] = self.to_python([condition, block])

        orelse = []

        for e in else_list[:: -1]:
            if isinstance(e, IfThenBranch):
                if isinstance(orelse, list):
                    if len(orelse) > 0:
                        e.orelse.append(orelse[0])
                else:
                    e.orelse.append(orelse)
                orelse = [e]
            else:
                orelse = e

        orelse = self.to_python(orelse) if isinstance(orelse, Block) else [
            self.to_python(e) for e in orelse]
        return ast.If(test=condition, body=block, orelse=orelse)

    def ifthenbranch(self, condition, block, orelse) -> ast.If:
        """ Translated to a Python If statement, which has the same structure as in SetlX """
        [condition, block] = self.to_python([condition, block])
        if len(orelse) > 0:
            if isinstance(orelse[0], Block):
                else_list = self.to_python(orelse[0])
            else:
                else_list = [self.to_python(e) for e in orelse]
        else:
            else_list = []

        return ast.If(test=condition, body=block, orelse=else_list)

    def implication(self, left, right) -> ast.Compare:
        """ "x => y" is translated to "not x or y" """
        [left, right] = self.to_python([left, right])
        not_left = ast.UnaryOp(op=ast.Not(), operand=left)
        return ast.Compare(left=not_left, ops=[ast.Or()], comparators=[right])

    def integerdivision(self, left, right) -> ast.BinOp:
        """ same in SetlX and Python (\\) """
        return self._binop(left, ast.FloorDiv(), right)

    def integerdivisionassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ same in SetlX and Python (\\=) """
        return self._augassign(assignable, ast.FloorDiv(), right_hand_side)

    def iterator_from_chain(self, iter_chain: list):
        """ This function converts a list of iterators.

        If the iterator chain only consists of one iterator, it can be converted to a python generator.
        The function returns this as a python expression.
        e.g.::

            x*2 : x in a

        is translated to::

            x*2 for x in a 

        In setlX iterators can be chained together like so::

            [x,y]: x in a, y in b

        this is translated via the function setlx.cartesian_product which creates a possible combinations::

            [x,y] for (x,y) in setlx.cartesian_product(a,b)
        
        """
        if len(iter_chain) == 1:
            return self.to_python([iter_chain[0].assignable, iter_chain[0].expression])

        assignables = [self.to_python(i.assignable) for i in iter_chain]
        assignable = ast.List(elts=assignables)

        exprs = [self.to_python(e.expression) for e in iter_chain]
        list_product = self.setlx_function("cartesian_product", exprs)

        return [assignable, list_product]

    def lambdaclosure(self, params, expr) -> ast.Lambda:
        """ Translated like LambdaProcedure (see lambdaprocedure method) """
        return self.lambdaprocedure(params, expr)

    def lambdadefinition(self, procedure, name: str) -> ast.Assign:
        """ Translated to assignment of lambda function

        e.g.::

            x := a,b |-> a*b;

        is translated to::

            x = lambda a,b: a*b
        """
        py_id = escape_id(name)
        lambda_py = self.lambdaprocedure(procedure.params, procedure.expr)
        return ast.Assign(targets=[ast.Name(id=py_id)], value=lambda_py)

    def lambdaprocedure(self, params: list, expr) -> ast.Lambda:
        """ Translated to Python Lambda 

        If the lambda is in the static block of a class, the parameter "self=None"
        is added to support a call as class function.
        """
        expr = self.to_python(expr)
        params = self.to_python(params)

        defaults = []
        if self.state.is_class_static():
            # add self=None as parameter in static class block
            params.append(ast.arg(arg="self", annotation=None))
            defaults.append(ast.NameConstant(None))

        return ast.Lambda(args=ast.arguments(args=params,
                                             vararg=None,
                                             kwonlyargs=[],
                                             kw_defaults=[],
                                             kwarg=None,
                                             defaults=defaults),
                          body=expr)

    def lessorequal(self, left, right) -> ast.Compare:
        """ Same in SetlX and Python (<=)"""
        return self._compare(left, ast.LtE(), right)

    def lessthan(self, left, right) -> ast.Compare:
        """ Same in SetlX and Python (<)"""
        return self._compare(left, ast.Lt(), right)

    def listparameter(self, id):
        raise "not reachable"

    def listrange(self, start, end) -> ast.Slice:
        """ same in SetlX and Python """
        [start, end] = self.to_python([start, end])
        return ast.Slice(lower=start, upper=end, step=None)

    def match(self):
        raise NotSupported("match is not supported")

    def memberaccess(self, parent, child) -> ast.Attribute:
        """ Translated to ast.Attribute (same in SetlX and Python)"""
        [parent, child] = self.to_python([parent, child])
        if isinstance(child, ast.Name):
            # unpack id to generate correct python ast
            child = child.id
        return ast.Attribute(value=parent, attr=child)

    def minus(self, expr) -> ast.UnaryOp:
        """ Same in SetlX and Python (-)"""
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.USub(), operand=expr)

    def modulo(self, left, right) -> ast.BinOp:
        """ Same in SetlX and Python (%)"""
        return self._binop(left, ast.Mod(), right)

    def moduloassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ Same as in python (%=) """
        return self._augassign(assignable, ast.Mod(), right_hand_side)

    def notequal(self, left, right) -> ast.Compare:
        """ Translated to python "!=" """
        return self._compare(left, ast.NotEq(), right)

    def notin(self, left, right) -> ast.Compare:
        """ Translated to python "not in" """
        return self._compare(left, ast.NotIn(), right)

    def operatorexpression(self, expr) -> ast.Starred:
        """ Translated to starred argument """
        expr = self.to_python(expr)
        return ast.Starred(value=expr)

    def parameter(self, id, default) -> ast.arg:
        """ Translated to ast.arg.

        The default parameter is not used since in python
        it is not stored in the argument but in a seperated list.
        """
        py_id = escape_id(id.id)
        if py_id in self.state.built_ins:
            del self.state.built_ins[self.state.built_ins.index(py_id)]
        self.state.variables.append(py_id)
        return ast.arg(arg=py_id, annotation=None)

    def power(self, base, exponent) -> ast.BinOp:
        """ "**" operator is same in python """
        return self._binop(base, ast.Pow(), exponent)

    def prefixoperator(self, expr, py_target_type) -> ast.Call:
        """ Helper function for generating a function call """
        expr = self.to_python(expr)
        return call_function(py_target_type, [expr])

    def procedure(self, params, block) -> ast.Name:
        """ Translated by defining a function in the statement before and using the functions name as translation

        e.g.::

            x := [procedure(a,b){...}]

        is translated to::

            def procedure_0_0(a,b):
                ...
            x = [procedure_0_0]
        """
        proc_name = f"procedure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(
            Procedure(params, block), proc_name))

        return ast.Name(id=proc_name)

    def proceduredefinition(self, procedure, name: str) -> ast.FunctionDef:
        """ This function creates a function definition with the given name and the content of the given procedure

        The function has the same params and block like the procedure.
        If it is a class method, the parameter "self" is added as first parameter.
        If it is a static class function the decorator "staticmethod" is used.   
        If the function is a cached procedure the decorator setlx.cached_procedure is used to mimic this functionality.
        At the beginning of the function all parameters that are not read-write-parameters are copied in order to make the 
        functions call by value.
        e.g.::

            test := cachedProcedure(x,y, rw A){
                ..
            };

        is translated to::

            @setlx.cached_procedure
            def test(x,y,A: 'rw'):
                [x,y] = setlx.copy([x,y])
                ...

        """
        py_name = escape_id(name)
        self.state.procedure_counter += 1

        [params, block] = procedure

        py_params = []
        defaults = []  # default values for parameters
        vararg = None
        value_params = []
        for p in params:
            if not isinstance(p, ListParameter):
                prm = self.to_python(p)
                if not isinstance(p, ReadWriteParameter):  # only copy value parameters
                    value_params.append(prm.arg)
                    if p.default != None:  # add default value if one is given
                        defaults.append(self.to_python(p.default))
                py_params.append(prm)
            else:
                py_id = self.to_python(p.id)
                value_params.append(py_id.id)
                vararg = ast.arg(arg=py_id.id, annotation=None)

        decorators = [self.setlx_access("cached_procedure")] if isinstance(
            procedure, CachedProcedure) else []

        if self.state.is_class_static():
            # if function is static, add self=None as optinal parameter to the end
            py_params.append(ast.arg(arg="self", annotation=None))
            defaults.append(ast.NameConstant(value=None))
            decorators.insert(0, ast.Name(id="staticmethod"))
        elif self.state.class_context != None:
            # add self.function_name = function name to make it a method
            self.state.class_context.variables.append(py_name)
            py_params.insert(0, ast.arg(arg="self", annotation=None))

        arguments = ast.arguments(args=py_params,
                                  vararg=vararg,
                                  kwonlyargs=[],
                                  kw_defaults=[],
                                  kwarg=None,
                                  defaults=defaults)

        block = self.to_python(block)
        if len(value_params) > 0:
            # deep copy parameters to allow call by value
            block.insert(0, self.copy_params(value_params))

        self.state.check_built_ins(py_name)
        self.state.procedures[py_name] = params
        return ast.FunctionDef(name=py_name, args=arguments, body=block, decorator_list=decorators, returns=None)

    def product(self, left, right) -> ast.BinOp:
        """ same in python """
        return self._binop(left, ast.Mult(), right)

    def productassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ "*=" is same in python """
        return self._augassign(assignable, ast.Mult(), right_hand_side)

    def productofmembers(self, expr) -> ast.Call:
        """ Translated by calling the function product with the expression as argument

        e.g. */[1,2] -> product([1,2])
        """
        return self._prefix_operator("product", expr)

    def productofmembersbinary(self, left, right) -> ast.Call:
        """ Translated by calling the function setlx.product with the left and right side as arguments

        e.g. 2 */[1,2] -> setlx.product([1,2], 2)
        """
        [left, right] = self.to_python([left, right])
        return self.setlx_function("product", [right, left])

    def quotient(self, left, right) -> ast.BinOp:
        """ "/"-perator is same in python """
        return self._binop(left, ast.Div(), right)

    def quotientassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ "/=" is same in python """
        return self._augassign(assignable, ast.Div(), right_hand_side)

    def range(self, start, step, end) -> ast.Call:
        """ translated with setlx._range function 

        Step is calculated by substrating the second from the first expression.
        e.g. [1,3..10] -> setlx._range(1, 10, 3-1)
        """
        [start, end] = self.to_python([start, end])
        range_params = [start, end]

        if step != None:
            # calculate step by substracting step from start
            py_step = ast.BinOp(left=self.to_python(
                step), op=ast.Sub(), right=start)
            range_params.append(py_step)

        return self.setlx_function("_range", range_params)

    def readwriteparameter(self, id) -> ast.arg:
        """ Translated as normal arugment (ast.arg) with "rw" annotation """
        py_id = self.to_python(id)
        return ast.arg(arg=py_id.id, annotation=ast.Str("rw"))

    def scan(self):
        raise NotSupported("scan is not supported")

    def setlistconstructor(self, collection) -> ast.Call:
        """ Translated by calling setlx.Set(...) with collection as argument

        e.g. {1,2,3} -> setlx.Set([1,2,3])
        """
        elts = []
        if collection == None:
            elts = []
        else:
            py_collection = self.to_python(collection)
            if isinstance(collection, Range):
                elts = [py_collection]
            else:
                elts = [py_collection.args[0]]
        return self.setlx_function("Set", elts)

    def setliteration(self, expr, iter_chain, condition) -> ast.Call:
        """ Translated to setlx.List with generator as argument"""
        iter_chain = self.to_python(iter_chain)
        expr = self.to_python(expr)
        condition = [self.to_python(condition)] if condition != None else []

        iter_chain[-1].ifs = condition
        return self.setlx_function("List", [ast.ListComp(elt=expr, generators=iter_chain)])

    def setliterator(self, assignable, expression) -> ast.comprehension:
        """ Translated with python equivalent which is a comprehension"""
        [assignable, expression] = self.to_python([assignable, expression])
        return ast.comprehension(target=assignable, iter=expression, ifs=[], is_async=0)

    def setlvector(self, values):
        """ Translated by calling setlx.Vector constructor with values as argument

        e.g. << 1 2 >> -> setlx.Vector([1,2]) 
        """
        py_values = self.to_python(values)
        return self.setlx_function("Vector", py_values)

    def setlmatrix(self, vectors):
        """ Translated by calling setlx.Matrix constructor with vectors as argument

        e.g. << << 1 2 >> << 2 1 >> >> -> setlx.Matrix([[1,2],[2,1]]) 
        """
        py_vec = [ast.List(elts=self.to_python(v.values)) for v in vectors]
        return self.setlx_function("Matrix", [ast.List(elts=py_vec)])

    def setlxassert(self, condition, expr) -> ast.Assert:
        """ Translated to Python Assert statement """
        [condition, expr] = self.to_python([condition, expr])
        return ast.Assert(test=condition, msg=expr)

    def setlxbreak(self) -> ast.Break:
        """ Translated to Python Break statement """
        return ast.Break()

    def setlxcontinue(self) -> ast.Continue:
        """ Translated to Python Continue statement """
        return ast.Continue()

    def setlxdouble(self, value: str) -> ast.Num:
        """ Translated as a Python number """
        return ast.Num(n=float(value))

    def setlxfalse(self) -> ast.NameConstant:
        """ Translates "true" to "True" """
        return bool_false()

    def setlxfor(self, iteratorChain, condition, block):
        """ Translates SetlX For to Python For

        Python does not support a conditions in for loops
        so they are translated as seperate if statement in loop.
        e.g.::

            for(x in list | x > 2){...}

        translated to::

            for x in list:
                if x > 2:
                    ...
        """
        block = self.to_python(block)
        [assignable, iterator] = self.iterator_from_chain(iteratorChain)
        # add condition as if self.statement in branch
        if condition != None:
            condition = self.to_python(condition)
            if_stmt = ast.If(test=condition, body=block, orelse=[])
            block = [if_stmt]
        return ast.For(target=assignable, iter=iterator, body=block, orelse=[])

    def setlxfraction(self, number: str) -> ast.Num:
        """ Translated as a Python number """
        return ast.Num(n=int(number))

    def setlxin(self, left, right) -> ast.Compare:
        """ Translated with Python in keyword """
        return self._compare(left, ast.In(), right)

    def setlxlist(self, cb) -> ast.Call:
        """ Translated by calling setlx.List(..) with list as argument

        e.g. [1,2,3] -> setlx.List([1,2,3])
        """
        elts = []
        if cb != None:
            elts = [self.to_python(cb)]
            if isinstance(cb, (ExplicitList, ExplicitListWithRest, SetlIteration)):
                return elts[0]
        return self.setlx_function("List", elts)

    def setlxliteral(self, value: str) -> ast.Str:
        """ Translated with Python string, stripping the "'" at start and beginning """
        # cut " from start and end
        return ast.Str(s=value[1: -1])

    def setlxnot(self, expr) -> ast.UnaryOp:
        """ Translated with Python not keyword """
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.Not(), operand=expr)

    def setlxom(self) -> ast.NameConstant:
        """ Translated with Python None """
        return ast.NameConstant(None)

    def setlxreturn(self, expression) -> ast.Return:
        """ Translated with Python return statement """
        expression = self.to_python(expression)
        return ast.Return(value=expression, decorator_list=[], returns=None)

    def setlxstring(self, string: str) -> ast.Str:
        """ This function translates setlx to python strings
        
        This can be quite complicated due to the fact that setlx strings can include expressions.
        In order to support this in python f-strings are beeing used.
        Since the expressions are not recognized by the parser, we need to recognize the expressions in here.
        e.g.::

            "$x$ + $y$ = $x+y$"

        is translated to::

            f'{x} + {y} = {x+y}'

        """
        value = string[1:-1]
        if len(value) == 0:
            # if the string is empty, so is the python string
            return ast.Str(s="")
        value = value.replace("\\n", "\n").replace(
            "\\t", "\t").replace("\\\"", "\"").replace("\\'", "s")
        # split string by expressions in string
        # e.g. "test $x$ = $x$" => ["test","$x$"," = ","$x$"]
        matches = re.finditer(r'\$(?!\\)[^$]+\$', value)
        indices = []
        for i in matches:
            indices += i.span()

        if len(indices) == 0:
            return ast.Str(s=value)

        if indices[0] != 0:
            indices.insert(0, 0)

        slices = [value[i:j] for i, j in zip(
            indices, indices[1:]+[None]) if len(value[i:j]) > 0]

        values = []
        for s in slices:
            if s[0] == "$":
                newline = "\n"
                tab = "\t"
                if len(s) == 1 or s[-1] != "$":
                    raise SyntaxError(
                        f'Error(s) while parsing string "{value}" {"{"}{newline}{tab}{"$ missing"}{newline}{"}"}')

                # escape backslashes
                escaped = codecs.unicode_escape_decode(s.strip("$"))[0]
                try:
                    setlx_expr = parse_expr(escaped)
                except Exception as e:
                    raise SyntaxError(
                        f'Error(s) while parsing string "{value}" {"{"}{newline}{tab}{e}{newline}{"}"}')
                expr = self.to_python(setlx_expr)
                values.append(
                    ast.FormattedValue(
                        value=expr, conversion=-1,
                        format_spec=None)
                )
            else:
                values.append(ast.Str(s))
        if len(values) == 1 and isinstance(values[0], str):
            return ast.Str(s=values[0])
        else:
            return ast.JoinedStr(values=values)

    def setlxtrue(self):
        """ Translates "true" to "True" """
        return bool_true()

    def setlxwhile(self, condition, block):
        """ Translates while construct to python while """
        [py_condition, py_block] = self.to_python([condition, block])
        return ast.While(test=py_condition, body=py_block, orelse=[])

    def sum(self, left, right):
        """ Translates SetlX plus operator with python plus operator """
        return self._binop(left, ast.Add(), right)

    def sumassignment(self, assignable, right_hand_side) -> ast.AugAssign:
        """ Translates += statement with python += statement """
        return self._augassign(assignable, ast.Add(), right_hand_side)

    def sumofmembers(self, expr) -> ast.Call:
        """ Translated by calling the function sum with the expression as argument"""
        return self._prefix_operator("sum", expr)

    def sumofmembersbinary(self, left, right) -> ast.Call:
        """ Translated by calling the function setlx.sum with the left and right side as arguments"""
        [left, right] = self.to_python([left, right])
        return self.setlx_function("sum", [right, left])

    def switch(self, case_list: list, default_branch) -> ast.If:
        """ Switch is translated to a list of if statements 

        A switch statement is translated to a list of if statements 
        where every value is checked if "elif" and the the default branch
        is represented by an else statement.

        If there only is a default branch no if is needed so the 
        translation of the default branch is returned
        """
        if len(case_list) == 0:
            # in setlx try can standalone, in python not
            return self.to_python(default_branch) or Block([])

        cond = self.to_python(case_list[0][0])
        blk = self.to_python(case_list[0][1])
        orelse = self.to_python(default_branch) or []

        for e in case_list[:: -2]:  # invert list and cut first element
            [test, block] = self.to_python(list(e[0:2]))
            orelse = [ast.If(test=test, body=block, orelse=orelse)]

        return ast.If(test=cond, body=blk, orelse=orelse)

    def term(self):
        raise NotSupported("terms are not supported")

    def trycatch(self, block: list, try_list: list) -> ast.Try:
        """ Translates a try catch construct 

        The translation is best described by an example::

            try{
                throw("error");
            } catchUsr(e){
                print("user error: $e$")
            } catchLng(e){
                print("language error: $e$")
            } catch(e){
                print("error: $e$")
            }

        This is translated to::

            try:
                setlx.throw("error");
            except setlx.UserExcetion as e:
                e = setlx.unpack_error(e)
                setlx.print(f"user error: {e}")
            except Exception as e:
                e = setlx.unpack_error(e)
                setlx.print(f"user error: {e}")
            except Exception as e:
                e = setlx.unpack_error(e)
                setlx.print(f"error: {e}")
        """
        block = self.to_python(block)
        if len(try_list) == 0:
            return block

        handlers = []
        for b in try_list:
            if isinstance(b, TryCatchUsrBranch):
                error_type = self.setlx_access("UserException")
            else:
                error_type = ast.Name(id="Exception")

            var = self.to_python(b.variable)
            error = self.unpack_error(var)
            except_block = [error] + self.to_python(b.block)
            ex = ast.ExceptHandler(
                type=error_type,
                name="e",
                body=except_block
            )
            handlers.append(ex)

        return ast.Try(
            body=block,
            handlers=handlers,
            orelse=[],
            finalbody=[]
        )

    def trycatchbranch(self, variable, block):
        """ not reachable since the try-catch construct is translated as one """
        raise Exception("not reachable")

    def trycatchlngbranch(self, variable, block):
        """ not reachable since the try-catch construct is translated as one """
        raise Exception("not reachable")

    def trycatchusrbranch(self, variable, block):
        """ not reachable since the try-catch construct is translated as one """
        raise Exception("not reachable")

    def variable(self, id: str, standalone: bool):
        """ Translates a variable

        By default this is translated to a python variable (ast.Name),
        but there are two special cases:

        1.  If the variable is called "this" we need to translate it to the corresponding keyword which is "self".

        2.  If the transpiler is in a class and the variable is a class attribute 
            the variable needs to be prefixed with "self." to enable the attribute access in pythons

        """

        if id == "this":
            return ast.Name(id="self")

        # prefix variable with "v_" if the id is a python keyword
        py_id = escape_id(id)

        if standalone == True and self.state.is_class_variable(py_id) and py_id not in self.state.variables:
            return ast.Attribute(value=ast.Name(id="self"), attr=py_id)

        if py_id in self.state.built_ins:
            return self.setlx_access(py_id)

        return ast.Name(id=py_id)

    def variableignore(self):
        """ Translates a ignored SetlX variable to a "_" python variable """
        return ast.Name(id="_")

    def setlx_access(self, name):
        """ Generates a expression that accesses a variable from the setlx package """
        self.state.imports.add("setlx")
        return ast.Attribute(value=ast.Name(id="setlx"), attr=name)

    def setlx_function(self, name: str, args: list) -> ast.Call:
        """ Generates a expression that calls a given function from the setlx package """
        self.state.imports.add("setlx")
        return ast.Call(func=self.setlx_access(name), args=args, keywords=[])

    def unpack_error(self, target) -> ast.Assign:
        """ Generates a statement that unpacks the error object from a Exception

        In SetlX every object can be thrown as a exception.
        In Python all Exception musst be subclasses of Exception.
        This statement unpacks the error that is inside a exception.
        e.g.::

            e = setlx.unpack_error(e)

        """
        self.state.imports.add("setlx")
        unpack_call = self.setlx_function("unpack_error", [ast.Name(id='e')])
        self.state.variables.append(target.id)
        return ast.Assign(targets=[target], value=unpack_call)

    def to_method(self, id: str, static: bool) -> ast.Assign:
        """ Generates a statement that converts a static class function to a none static one

        In SetlX static class functions can be called as instance methods.
        To enable this in python, the static functions are overriden with 
        a none static one in the init function.
        This statement does the overriding
        e.g. self.function = setlx.to_method(self,ClassName.function)
        """
        args = [ast.Name(id="self")]
        if static:
            args.append(ast.Attribute(
                value=ast.Name(
                    id=self.state.class_context.id), attr=id)
            )
            args.append(bool_true())
        else:
            args.append(ast.Name(id=id))

        return ast.Assign(
            targets=[ast.Attribute(
                value=ast.Name(id='self'),
                attr=id
            )],
            value=self.setlx_function("to_method", args)
        )

    def copy_params(self, params: list) -> ast.Assign:
        """ Creates the ast structure for deep copying procedure parameters

        This structure is used to copy all parameters at the beginning of a function.
        e.g. For the parameters x,y,z the code looks like this::

            [x,y,z] = setlx.copy([x,y,z])

        Parameters
        ----------
        params : list
            A list of strings with the name of the parameters 
        """
        elts = ast.List(elts=[ast.Name(p) for p in params])
        return ast.Assign(targets=[elts],
                          value=self.setlx_function("copy", [elts]))


class ParserErrorListener(ErrorListener):
    """ An ANTLR error listener that only raises syntax errors """

    def __init__(self):
        ErrorListener.__init__(self)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """ Raises a SyntaxError with the line, collumn and message as information """
        raise SyntaxError("line " + str(line) + ":" + str(column) + " " + msg)


def parse_input(input: InputStream) -> SetlXgrammarParser:
    """ Parses a input stream and returns the generated parser Object 

    Only syntax errors in the code are thrown (see ParserErrorListener)
    """
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    parser._listeners = [ParserErrorListener()]
    return parser


def parse_expr(string: str):
    """ Parses a Setlx-expression-string and returns the generated AST """
    input = InputStream(string)
    parser = parse_input(input)
    return parser.expr(False).ex


def call_function(name: str, params: list) -> ast.Call:
    """ Generates a ast for calling a function with parameters """
    return ast.Call(func=ast.Name(id=name), args=params, keywords=[])


def bool_true() -> ast.NameConstant:
    """ Returns the ast for "True" """
    return ast.NameConstant(value=True)


def bool_false() -> ast.NameConstant:
    """ Returns the ast for "False" """
    return ast.NameConstant(value=False)


def escape_id(id: str) -> str:
    """ Some ids in Setlx code might be Python keywords.
        To avoid syntax errors, these ids are prefixed with "v_"
    """
    return f"v_{id}" if id in keyword.kwlist+["setlx"] else id


def import_call(stlx_file: str) -> ast.ImportFrom:
    """ Generates a ast structure for importing the given setlx file

    The function takes a SetlX file import, strips the .stlx extension and replaces all "-" 
    with underscores. 
    e.g. "depth-first-search.stlx" -> depth_first_search

    Based on this generated module name a wildcard import statement is generated.
    e.g. from depth_first_search import *
    """
    if stlx_file[-5:len(stlx_file)] == ".stlx":
        file = stlx_file[0:-5]
    file = file.replace("-", "_")
    return ast.ImportFrom(module=file, names=[ast.alias(name='*', asname=None)], level=0)


class NotSupported(Exception):
    """ This exception is thrown when a lexical element is not supported """

    def __init__(self, msg=""):
        Exception.__init__(self, msg)
