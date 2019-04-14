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
    def __init__(self, root):
        self.root = root
        self.state = TranspilerState()

    def transpile(self):
        body = self.to_python(self.root)
        imports = self.state.imports.to_python(self.state)
        return imports + body

    def to_python(self, node):
        if node == None:
            return None
        if not isinstance(node, list):
            name = node.__class__.__name__.lower()
            return getattr(self, name)(*list(node))
        else:
            py_nodes = []
            for n in node:
                name = n.__class__.__name__.lower()
                py_nodes.append(getattr(self, name)(*list(n)))
            return py_nodes

    def _prefix_operator(self, operation, expr):
        expr = self.to_python(expr)
        return self.setlx_function(operation, [expr])

    def _binop(self, left, operator, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, operator, right)

    def _compare(self, left, operator, right):
        [left, right] = self.to_python([left, right])
        return ast.Compare(left=left, ops=[operator], comparators=[right])

    def _boolop(self, left, operator, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.BoolOp(op=operator, values=[left, right])

    def _augassign(self, assignable, operator, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=operator, value=rhs)

    def assignablecollectionaccess(self, assignable, exprs):
        assignable = self.to_python(assignable)
        if len(exprs) > 1:
            index = ast.Index(value=ast.List(elts=self.to_python(exprs)))
        else:
            expr = self.to_python(exprs[0])
            index = ast.Index(value=expr)
        return ast.Subscript(value=assignable, slice=index)

    def assignableignore(self):
        return ast.Name(id="_")

    def assignablelist(self, assignables):
        assignables = [self.to_python(a) for a in assignables]
        return ast.List(elts=assignables)

    def assignablemember(self, assignable, member):
        [target, member] = self.to_python([assignable, member])
        if assignable.id == "self":
            self.state.variables.append(assignable.member)
        return ast.Attribute(value=target, attr=member)

    def assignablevariable(self, id):
        py_id = escape_id(id)
        self.state.check_built_ins(py_id)
        if py_id == "this":
            id_str = "self"
        else:
            id_str = py_id
            self.state.variables.append(id_str)

        if self.state.class_context != None:
            self.state.class_context.variables.append(py_id)

        return ast.Name(id=id_str)

    def assignment(self, assignables, right_hand_side):
        left = self.to_python(assignables)
        right = self.to_python(right_hand_side)

        if isinstance(right, ast.Expr) and isinstance(right.value, ast.Call):
            right = right.value  # TODO fix this workaround. see tests/procedure

        return ast.Assign(targets=left, value=right)

    def backtrack(self):
        return ast.Raise(
            exc=self.setlx_function("BacktrackException", []),
            cause=None
        )

    def block(self, stmnts):
        # copy state variables to restore them after block translation
        variables = self.state.variables[:]
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

    def _bool_op(self, left, operator, right):
        [left_cond, right_cond] = self.to_python([left, right])
        left = call_function("bool", [left_cond])
        right = call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[operator], comparators=[right])

    def booleanequal(self, left, right):
        return self._bool_op(left, ast.Eq(), right)

    def booleannotequal(self, left, right):
        return self._bool_op(left, ast.NotEq(), right)

    def cachedprocedure(self, params, block):
        proc_name = f"procedure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(CachedProcedure(params,block),proc_name))
        
        return ast.Name(id=proc_name)

    def cardinality(self, expr):
        expr = self.to_python(expr)
        return call_function("len", [expr])

    def cartesianproduct(self, left, right):
        params = self.to_python([left, right])
        return self.setlx_function("cartesian_product", params)

    def check(self, check_block, backtrack_block):
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

    def classconstructor(self, id, params, block, static_block):
        static_block = static_block or []  # convert None to empty list

        py_id = escape_id(id)
        self.state.check_built_ins(py_id)

        self.state.class_context = ClassContext(py_id)

        params = self.to_python(params)
        body = self.to_python(block)
        for i, s in enumerate(body):
            if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name):
                if isinstance(s.targets[0], ast.Name):
                    s.targets[0] = s.targets[0].id
                s.targets = [
                    ast.Attribute(
                        value=ast.Name(id='self'),
                        attr=s.targets[0]
                    ),
                    ast.Name(id=s.targets[0])
                ]
            # enumerate over all generated functions and assign them as class method
            # e.g. self.method = method
            if isinstance(s, ast.FunctionDef):
                assign = ast.Assign(
                    targets=[ast.Attribute(
                        value=ast.Name(id='self'),
                        attr=s.name
                    )],
                    value=ast.Name(id=s.name)
                )
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
                assign = self.to_method(s.name)
                body.insert(0, assign)
            # check for all static lambda definitions and make them none static
            elif isinstance(s, ast.Assign) and isinstance(s.value, ast.Lambda):
                assign = self.to_method(s.targets[0].id)
                body.insert(0, assign)

        self_arg = ast.arg(arg='self', annotation=None)

        init = []
        if len(body) > 0:
            """ add init function for class
                example:
                    @setlx.procedure
                    def __init__(self,x,y):
                        ...
            """
            init.append(ast.FunctionDef(name='__init__',
                                        args=ast.arguments(
                                            args=[self_arg]+params,
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[]),
                                        body=body,
                                        decorator_list=[
                                            self.setlx_access("procedure")],
                                        returns=None))

        self.state.class_context = None
        return ast.ClassDef(
            name=py_id,
            bases=[],
            keywords=[],
            body=static+init,
            decorator_list=[]
        )

    def closure(self, params, block):
        warn("closures are translated as normal python functions, so they can only read from variables outside the scope")
        proc_name = f"closure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(Closure(params,block),proc_name))
 
        return ast.Name(id=proc_name)

    def collectionaccess(self, params, callable):
        callable = self.to_python(callable) if callable != None else None

        if isinstance(params, list):
            py_params = ast.List(elts=[self.to_python(p) for p in params])
        else:
            py_params = self.to_python(params)
        if isinstance(params, ListRange):
            return ast.Subscript(value=callable, slice=py_params)
        else:
            index = ast.Index(value=py_params)
            return ast.Subscript(value=callable, slice=index)

    def collectmap(self, expr, callable):
        access = self.to_python(CollectionAccess(expr, callable))
        return self.setlx_function("map", [access])

    def condition(self, expression):
        return self.to_python(expression)

    def conjunction(self, left, right):
        return self._boolop(left, ast.And(), right)

    def difference(self, left, right):
        return self._binop(left, ast.Sub(), right)

    def differenceassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.Sub(), right_hand_side)

    def disjunction(self, left, right):
        return self._boolop(left, ast.Or(), right)

    def dowhile(self, condition, block):
        [condition, block] = self.to_python([condition, block])
        break_block = [ast.Break()]
        negate = ast.UnaryOp(op=ast.Not(), operand=condition)
        if_break = ast.If(test=negate, body=break_block, orelse=[])
        block.append(if_break)
        return ast.While(test=bool_true(), body=block, orelse=[])

    def equal(self, left, right):
        return self._compare(left, ast.Eq(), right)

    def exists(self, iter_chain, condition):
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        expr = expr.args[0]  # unpack list from setlx.List object
        return call_function("any", [ast.GeneratorExp(elt=expr.elt, generators=expr.generators)])

    def exit(self):
        return call_function("exit", [])

    def explicitlist(self, exprs):
        list_arg = ast.List(elts=self.to_python(exprs))
        return self.setlx_function("List", [list_arg])

    def explicitlistwithrest(self, exprs, rest):
        py_exprs = self.to_python(exprs)
        py_exprs.append(ast.Starred(
            value=self.to_python(rest)
        ))
        return ast.List(elts=py_exprs)

    def factorial(self, expr):
        expr = self.to_python(expr)
        return self.setlx_function("factorial", [expr])

    def forall(self, iter_chain, condition):
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        expr = expr.args[0]  # unpack list from setlx.List object
        return call_function("all", [ast.GeneratorExp(elt=expr.elt, generators=expr.generators)])

    def functioncall(self, params, callable):
        params = [self.to_python(p) for p in params]

        """ TODO find proper way to handle this

        if isinstance(callable, Variable) and callable.id == "load":
            import_stmnt = import_call(callable.id)
            self.state.before_stmnts.append(
                WithLevel(self.state.level, import_stmnt))
            return None

        if callable.id == "eval":
            return ast.Call(func=ast.Attribute(value=ast.Name(id='setlx'), attr='eval'),
                            args=[params[0],
                                  ast.Call(func=ast.Name(id='globals'),
                                           args=[], keywords=[]),
                                  ast.Call(func=ast.Name(id='locals'), args=[], keywords=[])],
                            keywords=[])
        """
        expr = self.to_python(callable)
        return ast.Call(expr, params, [])

    def greaterorequal(self, left, right):
        return self._compare(left, ast.GtE(), right)

    def greaterthan(self, left, right):
        return self._compare(left, ast.Gt(), right)

    def ifthen(self, condition, block, else_list):
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

    def ifthenbranch(self, condition, block, orelse):
        [condition, block] = self.to_python([condition, block])
        if len(orelse) > 0:
            if isinstance(orelse[0], Block):
                else_list = self.to_python(orelse[0])
            else:
                else_list = [self.to_python(e) for e in orelse]
        else:
            else_list = []

        return ast.If(test=condition, body=block, orelse=else_list)

    def implication(self, left, right):
        [left, right] = self.to_python([left, right])
        not_left = ast.UnaryOp(op=ast.Not(), operand=left)
        return ast.Compare(left=not_left, ops=[ast.Or()], comparators=[right])

    def integerdivision(self, left, right):
        return self._binop(left, ast.FloorDiv(), right)

    def integerdivisionassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.FloorDiv(), right_hand_side)

    def iterator_from_chain(self, iter_chain):
        if len(iter_chain) == 1:
            return self.to_python([iter_chain[0].assignable, iter_chain[0].expression])

        assignables = [self.to_python(i.assignable) for i in iter_chain]
        assignable = ast.List(elts=assignables)

        exprs = [self.to_python(e.expression) for e in iter_chain]
        list_product = self.setlx_function("cartesian_product", exprs)

        return [assignable, list_product]

    def lambdaclosure(self, params, expr):
        return self.lambdaprocedure(params, expr)

    def lambdaprocedure(self, params, expr):
        expr = self.to_python(expr)
        params = self.to_python(params)

        defaults = []
        if self.state.is_class_static():
            params.append(ast.arg(arg="self", annotation=None))
            defaults.append(ast.NameConstant(None))

        return ast.Lambda(args=ast.arguments(args=params,
                                             vararg=None,
                                             kwonlyargs=[],
                                             kw_defaults=[],
                                             kwarg=None,
                                             defaults=defaults),
                          body=expr)

    def lessorequal(self, left, right):
        return self._compare(left, ast.LtE(), right)

    def lessthan(self, left, right):
        return self._compare(left, ast.Lt(), right)

    def listparameter(self, id):
        raise "not reachable"

    def listrange(self, start, end):
        start = self.to_python(start) if start != None else None
        end = self.to_python(end) if end != None else None
        return ast.Slice(lower=start, upper=end, step=None)

    def match(self):
        raise NotSupported("match is not supported")

    def memberaccess(self, parent, child):
        parent = self.to_python(parent)
        child = self.to_python(child)
        if isinstance(child, ast.Name):
            child = child.id
        return ast.Attribute(value=parent, attr=child)

    def minus(self, expr):
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.USub(), operand=expr)

    def modulo(self, left, right):
        return self._binop(left, ast.Mod(), right)

    def moduloassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.Mod(), right_hand_side)

    def notequal(self, left, right):
        return self._compare(left, ast.NotEq(), right)

    def notin(self, left, right):
        return self._compare(left, ast.NotIn(), right)

    def operatorexpression(self, expr):
        expr = self.to_python(expr)
        return ast.Starred(value=expr)

    def parameter(self, id, default):
        py_id = escape_id(id.id)
        if py_id in self.state.built_ins:
            del self.state.built_ins[self.state.built_ins.index(py_id)]
        self.state.variables.append(py_id)
        return ast.arg(arg=py_id, annotation=None)

    def power(self, base, exponent):
        return self._binop(base, ast.Pow(), exponent)

    def prefixoperator(self, expr, py_target_type):
        expr = self.to_python(expr)
        return call_function(py_target_type, [expr])

    def procedure(self, params, block):
        proc_name = f"procedure_{self.state.level}_{self.state.procedure_counter}"

        self.state.add_before(self.proceduredefinition(Procedure(params,block),proc_name))
 
        return ast.Name(id=proc_name)

    def proceduredefinition(self, procedure, name):
        self.state.procedure_counter += 1

        [params,block] = procedure
        decorator = self.setlx_access(
            "cached_procedure" if isinstance(procedure, CachedProcedure) else "procedure"
        )

        py_params = []
        defaults = []  # default values for parameters
        vararg = None
        for p in params:
            if not isinstance(p, ListParameter):
                prm = self.to_python(p)
                if isinstance(p, ReadWriteParameter):  # only copy value parameters
                    prm.annotation = ast.Str("rw")
                elif p.default != None:  # add default value if one is given
                    defaults.append(self.to_python(p.default))
                py_params.append(prm)
            else:
                py_id = self.to_python(p.id)
                vararg = ast.arg(arg=py_id.id, annotation=None)

        if self.state.is_class_static():
            # if function is static, add self=None as optinal parameter to the end
            py_params.append(ast.arg(arg="self", annotation=None))
            defaults.append(ast.NameConstant(value=None))

        arguments = ast.arguments(args=py_params,
                                  vararg=vararg,
                                  kwonlyargs=[],
                                  kw_defaults=[],
                                  kwarg=None,
                                  defaults=defaults)

        block = self.to_python(block)

        decorators = [ast.Name(id=decorator)] if isinstance(
            decorator, str) else [decorator]

        if self.state.is_class_static():
            decorators.insert(0, ast.Name(id="staticmethod"))

        py_name = escape_id(name)
        self.state.check_built_ins(py_name)
        self.state.procedures[py_name] = params
        return ast.FunctionDef(name=py_name, args=arguments, body=block, decorator_list=decorators, returns=None)


    def product(self, left, right):
        return self._binop(left, ast.Mult(), right)

    def productassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.Mult(), right_hand_side)

    def productofmembers(self, expr):
        return self._prefix_operator("product", expr)

    def productofmembersbinary(self, left, right):
        [left, right] = self.to_python([left, right])
        return self.setlx_function("product", [right, left])

    def quotient(self, left, right):
        return self._binop(left, ast.Div(), right)

    def quotientassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.Div(), right_hand_side)

    def range(self, start, step, end):
        start = self.to_python(start)
        end = self.to_python(end)
        range_params = [start, end]

        if step != None:
            step = ast.BinOp(left=self.to_python(
                step), op=ast.Sub(), right=start)
            range_params.append(step)

        return self.setlx_function("_range", range_params)

    def readwriteparameter(self, id):
        py_id = self.to_python(id)
        return ast.arg(arg=py_id.id, annotation=None)

    def scan(self):
        raise NotSupported("scan is not supported")

    def setlistconstructor(self, collection):
        if collection == None:
            return self.setlx_function("Set", [])
        else:
            py_collection = self.to_python(collection)
            if isinstance(collection, Range):
                return self.setlx_function("Set", [py_collection])
            elif isinstance(collection, SetlIteration):
                return self.setlx_function("Set", [py_collection.args[0]])
            else:
                # unpack setlx.List object
                return self.setlx_function("Set", [py_collection.args[0]])

    def setliteration(self, expr, iter_chain, condition):
        iter_chain = self.to_python(iter_chain)
        expr = self.to_python(expr)
        condition = [self.to_python(condition)] if condition != None else []

        iter_chain[-1].ifs = condition
        return self.setlx_function("List", [ast.ListComp(elt=expr, generators=iter_chain)])

    def setliterator(self, assignable, expression):
        [assignable, expression] = self.to_python([assignable, expression])
        return ast.comprehension(target=assignable, iter=expression, ifs=[], is_async=0)

    def setlvector(self, values):
        py_values = self.to_python(values)
        return self.setlx_function("Vector", py_values)

    def setlmatrix(self, vectors):
        py_vec = [ast.List(elts=self.to_python(v.values)) for v in vectors]
        return self.setlx_function("Matrix", [ast.List(elts=py_vec)])

    def setlxassert(self, condition, expr):
        [condition, expr] = self.to_python([condition, expr])
        return ast.Assert(test=condition, msg=expr)

    def setlxbreak(self):
        return ast.Break()

    def setlxcontinue(self):
        return ast.Continue()

    def setlxdouble(self, value):
        return ast.Num(n=float(value))

    def setlxfalse(self):
        return bool_false()

    def setlxfor(self, iteratorChain, condition, block):
        block = self.to_python(block)
        [assignable, iterator] = self.iterator_from_chain(iteratorChain)
        # add condition as if self.statement in branch
        if condition != None:
            condition = self.to_python(condition)
            if_stmt = ast.If(test=condition, body=block, orelse=[])
            block = [if_stmt]
        return ast.For(target=assignable, iter=iterator, body=block, orelse=[])

    def setlxfraction(self, number):
        num = int(number)
        return ast.Num(n=num)

    def setlxin(self, left, right):
        return self._compare(left, ast.In(), right)

    def setlxlist(self, cb):
        if cb != None:
            cb_py = self.to_python(cb)
            if isinstance(cb, ExplicitList):
                return cb_py
            if isinstance(cb, Range):
                return self.setlx_function("List", [cb_py])
            if isinstance(cb, SetlIteration):
                return cb_py
            return self.setlx_function("List", [cb_py])
        else:
            return self.setlx_function("List", [])

    def setlxliteral(self, value):
        if value.startswith("'") and value.endswith("'"):
            value = value[1: -1]
        return ast.Str(s=value)

    def setlxnot(self, expr):
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.Not(), operand=expr)

    def setlxom(self):
        return ast.NameConstant(None)

    def setlxreturn(self, expression):
        expression = self.to_python(expression)
        return ast.Return(value=expression, decorator_list=[], returns=None)

    def setlxstring(self, string):
        value = string.strip('"')
        if len(value) == 0:
            # if the string is empty, so is the python string
            return ast.Str(s="")

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
        return bool_true()

    def setlxwhile(self, condition, block):
        [condition, block] = self.to_python([condition, block])
        return ast.While(test=condition, body=block, orelse=[])

    def sum(self, left, right):
        return self._binop(left, ast.Add(), right)

    def sumassignment(self, assignable, right_hand_side):
        return self._augassign(assignable, ast.Add(), right_hand_side)

    def sumofmembers(self, expr):
        return self._prefix_operator("sum", expr)

    def sumofmembersbinary(self, left, right):
        [left, right] = self.to_python([left, right])
        return self.setlx_function("sum", [right, left])

    def switch(self, case_list, default_branch):
        if len(case_list) == 0:
            return default_branch
        else:
            cond = self.to_python(case_list[0][0])
            blk = self.to_python(case_list[0][1])
            orelse = []
            if default_branch is not None:
                orelse = self.to_python(default_branch)

            for e in case_list[:: -2]:  # cut first element
                c = self.to_python(e[0])
                b = self.to_python(e[1])
                orelse = [ast.If(test=c, body=b, orelse=orelse)]

            return ast.If(test=cond, body=blk, orelse=orelse)

    def term(self):
        raise NotSupported("terms are not supported")

    def trycatch(self, block, try_list):
        block = self.to_python(block)
        trys = len(try_list)
        if trys == 0:
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
        raise Exception("not reachable")

    def trycatchlngbranch(self, variable, block):
        raise Exception("not reachable")

    def trycatchusrbranch(self, variable, block):
        raise Exception("not reachable")

    def variable(self, id):
        # prefix variable with "v_" if the id is a python keyword
        py_id = escape_id(id)

        if py_id in self.state.built_ins:
            return self.setlx_access(py_id)

        if py_id == "this":
            py_id = "self"

        return ast.Name(id=py_id)

    def variableignore(self):
        return ast.Name(id="_")

    def setlx_access(self, name):
        self.state.imports.add("setlx")
        return ast.Attribute(value=ast.Name(id="setlx"), attr=name)

    def setlx_function(self, name, args):
        self.state.imports.add("setlx")
        return ast.Call(func=self.setlx_access(name), args=args, keywords=[])

    def unpack_error(self, target):
        self.state.imports.add("setlx")
        unpack_call = self.setlx_function("unpack_error", [ast.Name(id='e')])
        self.state.variables.append(target.id)
        return ast.Assign(targets=[target], value=unpack_call)

    def to_method(self, id):
        return ast.Assign(
            targets=[ast.Attribute(
                value=ast.Name(id='self'),
                attr=id
            )],
            value=self.setlx_function("to_method", [
                ast.Name(id="self"),
                ast.Attribute(value=ast.Name(
                    id=self.state.class_context.id), attr=id)
            ])
        )


class ParserErrorListener(ErrorListener):
    def __init__(self):
        ErrorListener.__init__(self)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line " + str(line) + ":" + str(column) + " " + msg)


def parse_input(input):
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    parser._listeners = [ParserErrorListener()]
    return parser


def parse_expr(string):
    input = InputStream(string)
    parser = parse_input(input)
    return parser.expr(False).ex


def call_function(name, params):
    return ast.Call(func=ast.Name(id=name), args=params, keywords=[])


def bool_true():
    return ast.NameConstant(value=True)


def bool_false():
    return ast.NameConstant(value=False)


def escape_id(id):
    """ Some ids in setlx code might be python keywords.
        To avoid syntax errors, these ids are prefixed with "v_"
    """
    return f"v_{id}" if id in keyword.kwlist+["setlx"] else id


def import_call(stlx_file):
    file = stlx_file.rstrip(".stlx")
    file = file.replace("-", "_")
    return ast.ImportFrom(module=file, names=[ast.alias(name='*', asname=None)], level=0)


class NotSupported(Exception):
    def __init__(self, msg=""):
        Exception.__init__(self, msg)
