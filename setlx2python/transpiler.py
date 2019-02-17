import ast
from .utils import *
from .grammar.types import *


class ImportList:
    def __init__(self):
        self.imports = []

    def add(self, module):
        if module not in self.imports:
            self.imports.append(module)

    def to_python(self, state):
        return [ast.Import(names=[ast.alias(name=i, asname=None)]) for i in self.imports]


class TranspilerState:
    def __init__(self):
        # current statement
        self.before_stmnts = []
        self.procedure_counter = 0
        # scope level
        self.level = 0
        # modules that need to be imported
        self.imports = ImportList()
        self.in_init = False


class Transpiler:
    def __init__(self, root):
        self.root = root
        self.state = TranspilerState()

    def transpile(self):
        body = self.to_python(self.root)
        imports = self.state.imports.to_python(self.state)
        return imports + body

    def to_python(self, node):
        if not isinstance(node, list):
            name = node.__class__.__name__.lower()
            return getattr(self, name)(*list(node))
        else:
            py_nodes = []
            for n in node:
                name = n.__class__.__name__.lower()
                py_nodes.append(getattr(self, name)(*list(n)))
            return py_nodes

    def lessorequal(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.LtE()], comparators=[right])

    def conjunction(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.BoolOp(op=ast.And(), values=[left, right])

    def greaterthan(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.Gt()], comparators=[right])

    def block(self, stmnts):
        procedure_counter = self.state.procedure_counter
        self.state.procedure_counter = 0

        py_stmnts = []
        for s in stmnts:
            level = self.state.level
            self.state.level += 1  # next depth level
            stmnt = self.to_python(s)
            self.state.level = level

            # TODO this needs a better solution
            if isinstance(stmnt, (ast.Compare, ast.UnaryOp, ast.BinOp, ast.Call, ast.Set, ast.SetComp)):
                stmnt = ast.Expr(value=stmnt)

            if len(self.state.before_stmnts) > 0:
                # prepend self.statements that need to be executed before self.statement (e.g. function declaration)
                before, not_before = [], []
                for x in self.state.before_stmnts:
                    # only append before self.statements that were generated in higher levels
                    (not_before, before)[x.level > self.state.level].append(x)

                py_stmnts += [self.to_python(b) for b in before]
                self.state.before_stmnts = not_before

            py_stmnts.append(stmnt)

        self.state.procedure_counter = procedure_counter
        return py_stmnts

    def backtrack(self):
        raise Exception("backtrack is not supported yet")

    def readwriteparameter(self, id):
        return ast.arg(arg=id, annotation=None)

    def exit(self):
        return call_function("exit", [])

    def differenceassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.Sub(), value=rhs)

    def lambdaclosure(self, params, expr):
        expr = self.to_python(expr)
        params = self.to_python(params)
        return ast.Lambda(args=ast.arguments(args=params,
                                             vararg=None,
                                             kwonlyargs=[],
                                             kw_defaults=[],
                                             kwarg=None,
                                             defaults=[]),
                          body=expr)

    def assignmentother(self, assignable, right_hand_side, operator):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=operator, value=rhs)

    def equal(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.Eq()], comparators=[right])

    def ifthen(self, condition, block, else_list):
        [condition, block] = self.to_python([condition, block])

        orelse = []
        
        for e in else_list[::-1]:
            if isinstance(e, IfThenBranch):
                if isinstance(orelse,list):
                    e.orelse.append(orelse[0])
                else:
                    e.orelse.append(orelse)
                orelse = [e]
            else:
                orelse = e

        orelse = self.to_python(orelse) if isinstance(orelse, Block) else [
            self.to_python(e) for e in orelse]
        return ast.If(test=condition, body=block, orelse=orelse)

    def setlxfor(self, iteratorChain, condition, block):
        block = self.to_python(block)
        [assignable, iterator] = self.iterator_from_chain(iteratorChain)
        # add condition as if self.statement in branch
        if condition != None:
            condition = self.to_python(condition)
            if_stmt = ast.If(test=condition, body=block, orelse=[])
            block = [if_stmt]
        return ast.For(target=assignable, iter=iterator, body=block, orelse=[])

    def exists(self, iter_chain, condition):
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        return call_function("any", [expr])

    def switch(self, case_list, default_branch):
        if len(case_list) == 0:
            return default_branch
        else:
            cond = self.to_python(case_list[0][0])
            blk = self.to_python(case_list[0][1])
            orelse = []
            if default_branch is not None:
                orelse = self.to_python(default_branch)

            for e in case_list[::-2]:  # cut first element
                c = self.to_python(e[0])
                b = self.to_python(e[1])
                orelse = [ast.If(test=c, body=b, orelse=orelse)]

            return ast.If(test=cond, body=blk, orelse=orelse)

    def prefixoperator(self, expr, py_target_type):
        expr = self.to_python(expr)
        return call_function(py_target_type, [expr])

    def trycatch(self, block, try_list):
        block = self.to_python(block)
        trys = len(try_list)
        if trys == 0:
            return block
        if trys == 1 and isinstance(try_list[0], TryCatchBranch):
            catch = try_list[0]
            error = unpack_error(self.state, catch.variable.id)
            except_block = [error] + self.to_python(catch.block)
            ex = ast.ExceptHandler(
                type=ast.Name(id="Exception"),
                name="e",
                body=except_block
            )
            return ast.Try(
                body=block,
                handlers=[ex],
                orelse=[],
                finalbody=[]
            )
        else:
            # TODO try_list
            raise "only one catch is supported"

    def procedure(self, params, block, name, decorator):
        block = self.to_python(block)
        stlx_params = params

        if decorator == None:
            decorator = setlx_access(self.state, "procedure")

        params = []
        defaults = []  # default values for parameters
        vararg = None
        for p in stlx_params:
            if not isinstance(p, ListParameter):
                prm = self.to_python(p)
                if isinstance(p, ReadWriteParameter):  # only copy value parameters
                    prm.annotation = ast.Str("rw")
                elif p.default != None:  # add default value if one is given
                    defaults.append(self.to_python(p.default))
                params.append(prm)
            else:
                vararg = ast.arg(arg=p.id, annotation=None)

        params = ast.arguments(args=params,
                               vararg=vararg,
                               kwonlyargs=[],
                               kw_defaults=[],
                               kwarg=None,
                               defaults=defaults)
        decorators = []
        if decorator != None:
            decorators = [ast.Name(id=decorator)] if isinstance(
                decorator, str) else [decorator]
        if name == None:
            # TODO find better naming
            proc_name = f"procedure_{self.state.level}_{self.state.procedure_counter}"

            self.state.before_stmnts.append(
                WithLevel(self.state.level, ast.FunctionDef(name=proc_name, args=params, body=block, decorator_list=decorators)))

            self.state.procedure_counter += 1
            return ast.Name(id=proc_name)
        else:
            return ast.FunctionDef(name=name, args=params, body=block, decorator_list=decorators, returns=None)

    def productofmembers(self, expr):
        expr = self.to_python(expr)
        return setlx_function(self.state, "product", [expr])

    def setlxtrue(self):
        return bool_true()

    def assignablelist(self, assignables):
        assignables = [self.to_python(a) for a in assignables]
        return ast.List(elts=assignables)

    def setlxbreak(self):
        return ast.Break()

    def lessthan(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.Lt()], comparators=[right])

    def difference(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.Sub(), right)

    def functioncall(self, params, callable):
        params = [self.to_python(p) for p in params]
        if isinstance(callable,Variable) and callable.id == "throw":
            return setlx_function(self.state,"throw",params)
        expr = self.to_python(callable)
        return ast.Call(expr, params, [])

    def factorial(self, expr):
        expr = self.to_python(expr)
        return call_function("factorial", [expr])

    def setlxnot(self, expr):
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.Not(), operand=expr)

    def productassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.Mult(), value=rhs)

    def cachedprocedure(self, params, block, name):
        decorator = setlx_access(self.state, "cached_procedure")
        return self.to_python(Procedure(params, block, name, decorator))

    def booleanequal(self, left, right):
        [left_cond, right_cond] = self.to_python([left, right])
        left = call_function("bool", [left_cond])
        right = call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.Eq()], comparators=[right])

    def trycatchbranch(self, variable, block):
        raise "not reachable"

    def setlxom(self):
        return ast.NameConstant(None)

    def forall(self, iter_chain, condition):
        expr = self.to_python(SetlIteration(condition, iter_chain, None))
        return call_function("all", [expr])

    def notequal(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.NotEq()], comparators=[right])

    def binoperator(self, left, right, operator):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, operator, right)

    def setlistconstructor(self, collection):
        # TODO use own sets
        if collection == None:
            return call_function("set", [])
        else:
            py_collection = self.to_python(collection)
            if isinstance(collection, Range):
                return call_function("set", [py_collection.args[0]])
            elif isinstance(collection, SetlIteration):
                return ast.SetComp(elt=py_collection.elt, generators=py_collection.generators)
            else:
                return ast.Set(elts=py_collection.elts)

    def compare(self, left, right, operator):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[operator], comparators=[right])

    def setlxfalse(self):
        return bool_false()

    def minus(self, expr):
        expr = self.to_python(expr)
        return ast.UnaryOp(op=ast.USub(), operand=expr)

    def dowhile(self, condition, block):
        [condition, block] = self.to_python([condition, block])
        break_block = [ast.Break()]
        negate = ast.UnaryOp(op=ast.Not(), operand=condition)
        if_break = ast.If(test=negate, body=break_block, orelse=[])
        block.append(if_break)
        return ast.While(test=bool_true(), body=block, orelse=[])

    def quotientassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.Div(), value=rhs)

    def explicitlist(self, exprs):
        return ast.List(elts=[self.to_python(e) for e in exprs])

    def setlxfunction(self, expr, py_target_type):
        expr = self.to_python(expr)
        return setlx_function(self.state, py_target_type, [expr])

    def modulo(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.Mod(), right)

    def setliterator(self, assignable, expression):
        [assignable, expression] = self.to_python([assignable, expression])
        return ast.comprehension(target=assignable, iter=expression, ifs=[], is_async=0)

    def disjunction(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.BoolOp(op=ast.Or(), values=[left, right])

    def setlxreturn(self, expression):
        expression = self.to_python(expression)
        return ast.Return(value=expression, decorator_list=[], returns=None)

    def variable(self, id):
        id_str = id if id != "this" else "self"
        return ast.Name(id=id_str)

    def sumofmembersbinary(self, left, right):
        expr = self.to_python(right)
        return setlx_function(self.state, "sum", [expr])

    def condition(self, expression):
        return self.to_python(expression)

    def cartesianproduct(self, left, right):
        params = self.to_python([left, right])
        return setlx_function(self.state, "cartesian_product", params)

    def setlxlist(self, expr):
        if expr != None:
            return self.to_python(expr)
        else:
            return ast.List(elts=[])

    def integerdivision(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.FloorDiv(), right)

    def integerdivisionassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.FloorDiv(), value=rhs)

    def product(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.Mult(), right)

    def sumassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.Add(), value=rhs)

    def sumofmembers(self, expr):
        expr = self.to_python(expr)
        return setlx_function(self.state, "sum", [expr])

    def moduloassignment(self, assignable, right_hand_side):
        [target, rhs] = self.to_python([assignable, right_hand_side])
        return ast.AugAssign(target=target, op=ast.Mod(), value=rhs)

    def cardinality(self, expr):
        expr = self.to_python(expr)
        return call_function("len", [expr])

    def assignment(self, assignable, right_hand_side):
        [left, right] = self.to_python([assignable, right_hand_side])
        # return (py_target_type)(left, right)
        if isinstance(right, ast.Expr) and isinstance(right.value, ast.Call):
            right = right.value  # TODO fix this workaround. see tests/procedure
        return ast.Assign(targets=[left], value=right)

    def setlxfraction(self, number):
        num = int(number)
        return ast.Num(n=num)

    def setlxcontinue(self):
        return ast.Continue()

    def productofmembersbinary(self, left, right):
        expr = self.to_python(right)
        return setlx_function(self.state, "product", [expr])

    def listparameter(self, id):
        raise "not reachable"

    def range(self, start, step, end):
        start = self.to_python(start)
        end = self.to_python(end)
        end_plus_one = ast.BinOp(left=end, op=ast.Add(), right=ast.Num(n=1))
        range_params = [start, end_plus_one]

        if step != None:
            step = ast.BinOp(left=self.to_python(
                step), op=ast.Sub(), right=start)
            range_params.append(step)

        range_call = call_function("range", range_params)
        return call_function("list", [range_call])

    def sum(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.Add(), right)

    def ifthenbranch(self, condition, block, orelse):
        [condition, block] = self.to_python([condition, block])
        else_list = self.to_python(orelse[0]) if isinstance(orelse[0], Block) else [
            self.to_python(e) for e in orelse]

        return ast.If(test=condition, body=block, orelse=else_list)

    def setlxstring(self, value):
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        return ast.Str(value)

    def operatorexpression(self, expr):
        expr = self.to_python(expr)
        return ast.Starred(value=expr)

    def implication(self, left, right):
        [left, right] = self.to_python([left, right])
        not_left = ast.UnaryOp(op=ast.Not(), operand=left)
        return ast.Compare(left=not_left, ops=[ast.Or()], comparators=[right])

    def parameter(self, id, default, read_write):
        return ast.arg(arg=id, annotation=None)

    def setlxliteral(self, value):
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        return ast.Str(s=value)

    def setlxwhile(self, condition, block):
        [condition, block] = self.to_python([condition, block])
        return ast.While(test=condition, body=block, orelse=[])

    def greaterorequal(self, left, right):
        left = self.to_python(left)
        right = self.to_python(right)
        return ast.Compare(left=left, ops=[ast.GtE()], comparators=[right])

    def classconstructor(self, id, params, block, static_block):
        body = self.to_python(block)
        for s in body:
            if isinstance(s, ast.Assign) and isinstance(s.targets[0],ast.Name):
                s.targets[0] = ast.Attribute(value=ast.Name(id='self'), attr=s.targets[0])

        for i, s in enumerate(body):
            if isinstance(s, ast.FunctionDef):
                assign = ast.Assign(
                    targets=[ast.Attribute(
                        value=ast.Name(id='self'),
                        attr=s.name
                    )],
                    value=ast.Name(id=s.name)
                )
                body.insert(i+1, assign)

        params = self.to_python(params)
        self_arg = ast.arg(arg='self', annotation=None)
        static = self.to_python(static_block)
        make_funcs_static(static)
        func_decorator = setlx_access(self.state, "procedure")

        init = ast.FunctionDef(name='__init__',
                               args=ast.arguments(
                                   args=[self_arg]+params,
                                   vararg=None,
                                   kwonlyargs=[],
                                   kw_defaults=[],
                                   kwarg=None,
                                   defaults=[]),
                               body=body,
                               decorator_list=[func_decorator],
                               returns=None)
        return ast.ClassDef(
            name=id,
            bases=[],
            keywords=[],
            body=static+[init],
            decorator_list=[]
        )

    def collectionaccess(self, params, callable):
        callable = self.to_python(callable) if callable != None else None
        # params = [py_stmnt.Difference(p.to_python(
        #    self.state), py_type.PyFraction(1, 1)) for p in params]
        # TODO what if params is list?
        if isinstance(params, list):
            py_params = ast.List(elts=[self.to_python(p) for p in params])
        else:
            py_params = self.to_python(params)
        if isinstance(params, ListRange):  # TODO maby more elegant solution?
            return ast.Subscript(value=callable, slice=py_params)
        else:
            index = ast.Index(value=ast.BinOp(py_params, ast.Sub(), ast.Num(n=1)))
            return ast.Subscript(value=callable, slice=index)

    def booleannotequal(self, left, right):
        [left_cond, right_cond] = self.to_python([left, right])
        left = call_function("bool", [left_cond])
        right = call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.NotEq()], comparators=[right])

    def listrange(self, start, end):
        start = self.to_python(start) if start != None else None
        end = self.to_python(end) if end != None else None
        if start != None:
            start = ast.BinOp(left=start, op=ast.Sub(), right=ast.Num(1))
        return ast.Slice(lower=start, upper=end, step=None)

    def memberaccess(self, parent, child):
        parent = self.to_python(parent)
        child = self.to_python(child)
        return ast.Attribute(value=parent, attr=child)

    def assignablecollectionaccess(self, assignable, exprs):
        if len(exprs) > 1:
            raise Exception("only one collection access is allowed")
        [assignable, expr] = self.to_python([assignable, exprs[0]])
        index = ast.Index(value=ast.BinOp(
            left=expr, op=ast.Sub(), right=ast.Num(n=1)))
        return ast.Subscript(value=assignable, slice=index)

    def withlevel(self, level, code):
        return code

    def setliteration(self, expr, iter_chain, condition):

        iter_chain = self.to_python(iter_chain)
        expr = self.to_python(expr)
        condition = [self.to_python(condition)] if condition != None else []

        iter_chain[-1].ifs = condition
        return ast.ListComp(elt=expr, generators=iter_chain)

    def quotient(self, left, right):
        [left, right] = self.to_python([left, right])
        return ast.BinOp(left, ast.Div(), right)

    def setlxassert(self, condition, expr):
        [condition, expr] = self.to_python([condition, expr])
        return ast.Assert(test=condition, msg=expr)

    def iterator_from_chain(self, iter_chain):
        if len(iter_chain) == 1:
            return self.to_python([iter_chain[0].assignable, iter_chain[0].expression])

        assignables = [self.to_python(i.assignable) for i in iter_chain]
        assignable = ast.List(elts=assignables)

        exprs = [self.to_python(e.expression) for e in iter_chain]
        list_product = setlx_function(
            self.state, "cartesian_product", exprs)

        return [assignable, list_product]
