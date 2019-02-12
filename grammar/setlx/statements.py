from grammar.setlx.types import WithLevel
import grammar.setlx.utils as utils
from grammar.setlx.block import Block
import grammar.setlx.types as types
import ast


class Assignment:
    def __init__(self, assignable, right_hand_side):
        self.assignable = assignable
        self.right_hand_side = right_hand_side

    def to_python(self, state):
        [left, right] = utils.to_python(
            state, [self.assignable, self.right_hand_side])
        # return (self.py_target_type)(left, right)
        if isinstance(right, ast.Expr) and isinstance(right.value, ast.Call):
            right = right.value  # TODO fix this workaround. see tests/procedure
        return ast.Assign(targets=[left], value=right)


class AssignmentOther:
    def __init__(self, assignable, right_hand_side, operator):
        self.assignable = assignable
        self.right_hand_side = right_hand_side
        self.operator = operator

    def to_python(self, state):
        [target, rhs] = utils.to_python(
            state, [self.assignable, self.right_hand_side])
        return ast.AugAssign(target=target, op=self.operator, value=rhs)


class SumAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(
            self, assignable, right_hand_side, ast.Add())


class DifferenceAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(self, assignable, right_hand_side, ast.Sub())


class ProductAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(self, assignable, right_hand_side, ast.Mult())


class QuotientAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(self, assignable, right_hand_side, ast.Div())


class IntegerDivisionAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(
            self, assignable, right_hand_side, ast.FloorDiv())


class ModuloAssignment(AssignmentOther):
    def __init__(self, assignable, right_hand_side):
        AssignmentOther.__init__(self, assignable, right_hand_side, ast.Mod())


class Factorial:
    def __init__(self, expr):
        self.expr = expr

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return utils.call_function("factorial", [expr])


class FunctionCall:
    def __init__(self, params, expression):
        # maby later Call.__init__(self, None)
        self.params = params
        self.expression = expression
        self.callable = None

    def to_python(self, state):
        # TODO expression (unpack param)
        params = [p.to_python(state) for p in self.params]
        expr = self.callable.to_python(state)
        return ast.Expr(ast.Call(expr, params, []))


class Compare:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def to_python(self, state):
        left = self.left.to_python(state)
        right = self.right.to_python(state)
        return ast.Compare(left=left, ops=[self.operator], comparators=[right])


class Equal(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.Eq())


class GreaterThan(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.Gt())


class GreaterOrEqual(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.GtE())


class LessOrEqual(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.LtE())


class LessThan(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.Lt())


class NotEqual(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.NotEq())


class Disjunction(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.Or())

    def to_python(self, state):
        left = self.left.to_python(state)
        right = self.right.to_python(state)
        return ast.BoolOp(op=ast.Or(), values=[left, right])


class Conjunction(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.And())

    def to_python(self, state):
        left = self.left.to_python(state)
        right = self.right.to_python(state)
        return ast.BoolOp(op=ast.And(), values=[left, right])


class PrefixOperator:
    def __init__(self, expr, py_target_type):
        self.expr = expr
        self.py_target_type = py_target_type

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return utils.call_function(self.py_target_type, [expr])


class SumOfMembersBinary(PrefixOperator):
    def __init__(self, left, right):
        PrefixOperator.__init__(self, right, "sum")


class ProductOfMembersBinary(PrefixOperator):
    def __init__(self, left, right):
        # TODO create function for product
        PrefixOperator.__init__(self, right, "sum")


class SumOfMembers(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, "sum")


class ProductOfMembers(PrefixOperator):
    def __init__(self, expr):
        # TODO create function for product
        PrefixOperator.__init__(self, expr, "sum")


class Cardinality(PrefixOperator):
    def __init__(self, expr):
        # TODO create function for product
        PrefixOperator.__init__(self, expr, "len")


class Minus:
    def __init__(self, expr):
        self.expr = expr

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return ast.UnaryOp(op=ast.USub(), operand=expr)


class Forall:
    def __init__(self, iter_chain, condition):
        self.iter_chain = iter_chain
        self.condition = condition

    def to_python(self, state):
        expr = SetlIteration(
            self.condition, self.iter_chain, None).to_python(state)
        return utils.call_function("all", [expr])


class Exists:
    def __init__(self, iter_chain, condition):
        self.iter_chain = iter_chain
        self.condition = condition

    def to_python(self, state):
        expr = SetlIteration(
            self.condition, self.iter_chain, None).to_python(state)
        return utils.call_function("any", [expr])


class Not(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, "not")

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return ast.UnaryOp(op=ast.Not(), operand=expr)


class InfixOperator:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class BinOperator(InfixOperator):
    def __init__(self, left, right, operator):
        InfixOperator.__init__(self, left, right)
        self.operator = operator

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        return ast.BinOp(left, self.operator, right)


class Difference(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Sub())


class Sum(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Add())


class Product(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Mult())


class Quotient(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Div())


class IntegerDivision(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.FloorDiv())


class Modulo(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Mod())


class CartesianProduct(BinOperator):
    def __init__(self, left, right):
        BinOperator.__init__(self, left, right, ast.Mod())

    def to_python(self, state):
        state.imports.add("itertools", "product")
        params = utils.to_python(state, [self.left, self.right])
        return utils.call_function("product", params)


class IfThen:
    def __init__(self, condition, block, else_list=[]):
        self.else_list = else_list
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])

        orelse = []
        for e in self.else_list[::-1]:
            if isinstance(e, IfThenBranch):
                e.orelse = orelse
                orelse = [e]
            else:
                orelse = e

        orelse = orelse.to_python(state) if isinstance(orelse, Block) else [
            e.to_python(state) for e in orelse]
        return ast.If(test=condition, body=block, orelse=orelse)


class IfThenBranch:
    def __init__(self, condition, block, orelse=None):
        self.condition = condition
        self.block = block
        self.orelse = orelse

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        orelse = self.orelse.to_python(state) if isinstance(self.orelse, Block) else [
            e.to_python(state) for e in self.orelse]

        return ast.If(test=condition, body=block, orelse=orelse)


class Switch:
    def __init__(self, case_list, default_branch):
        self.case_list = case_list
        self.default_branch = default_branch

    def to_python(self, state):
        if len(self.case_list) == 0:
            return self.default_branch
        else:
            [cond, blk] = utils.to_python(state, self.case_list[0])
            orelse = []
            if self.default_branch is not None:
                orelse = self.default_branch.to_python(state)

            for e in self.case_list[::-2]:
                [c, b] = utils.to_python(state, e)
                orelse = [ast.If(test=c, body=b, orelse=orelse)]

            return ast.If(test=cond, body=blk, orelse=orelse)


class Condition:
    def __init__(self, expression):
        self.expression = expression

    def to_python(self, state):
        return self.expression.to_python(state)


class While:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        return ast.While(test=condition, body=block, orelse=[])


class DoWhile:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        break_block = [ast.Break()]
        negate = ast.UnaryOp(op=ast.Not(), operand=condition)
        if_break = ast.If(test=negate, body=break_block, orelse=[])
        block.append(if_break)
        return ast.While(test=utils.bool_true(), body=block, orelse=[])


class Backtrack:
    pass


class Break:
    pass


class Continue:
    pass


class Exit:
    pass


class Return:
    def __init__(self, expression):
        self.expression = expression

    def to_python(self, state):
        expression = self.expression.to_python(state)
        return ast.Return(value=expression, decorator_list=[], returns=None)


class For:
    def __init__(self, iteratorChain, condition, block):
        self.iteratorChain = iteratorChain
        self.condition = condition
        self.block = block

    def to_python(self, state):
        block = self.block.to_python(state)
        [assignable, iterator] = utils.iterator_from_chain(
            state, self.iteratorChain)
        # add condition as if statement in branch
        if self.condition != None:
            condition = self.condition.to_python(state)
            if_stmt = ast.If(test=condition, body=block, orelse=[])
            block = [if_stmt]
        return ast.For(target=assignable, iter=iterator, body=block, orelse=[])


class Procedure:
    def __init__(self, params, block, name=None):
        self.params = params
        self.block = block
        self.name = name

    def to_python(self, state):
        block = self.block.to_python(state)

        params = []
        deepcopies = []
        defaults = []  # default values for parameters
        for p in self.params:
            params.append(p.to_python(state))
            if not isinstance(p, types.ReadWriteParameter):  # only copy value parameters
                deepcopies.append(utils.deep_copy_param(
                    ast.Name(id=p.id), state))
                if p.default != None:  # add default value if one is given
                    defaults.append(p.default.to_python(state))

        block = deepcopies + block
        params = ast.arguments(args=params,
                               vararg=None,
                               kwonlyargs=[],
                               kw_defaults=[],
                               kwarg=None,
                               defaults=defaults)

        if self.name == None:
            # TODO find better naming
            proc_name = f"procedure_{state.level}_{state.procedure_counter}"

            state.before_stmnts.append(
                WithLevel(state.level, ast.FunctionDef(name=proc_name, args=params, body=block, decorator_list=[])))

            state.procedure_counter += 1
            return ast.Name(id=proc_name)
        else:
            return ast.FunctionDef(name=self.name, args=params, body=block, decorator_list=[])


class CachedProcedure:
    def __init__(self, params, block, name=None):
        self.params = params
        self.block = block
        self.name = name

    def to_python(self, state):
        return Procedure(self.params, self.block, self.name).to_python(state)


class CollectionAccess:
    def __init__(self, params):
        self.params = params
        self.callable = None

    def to_python(self, state):
        callable = self.callable.to_python(
            state) if self.callable != None else None
        # params = [py_stmnt.Difference(p.to_python(
        #    state), py_type.PyFraction(1, 1)) for p in self.params]
        # TODO what if params is list?
        params = self.params.to_python(state)
        if isinstance(self.params, types.ListRange):  # TODO maby more elegant solution?
            return ast.Subscript(value=callable, slice=params)
        else:
            index = ast.Index(value=ast.BinOp(params, ast.Sub(), ast.Num(n=1)))
            return ast.Subscript(value=callable, slice=index)


class SetlIteration:
    def __init__(self, expr, iter_chain, condition):
        self.expr = expr
        self.iter_chain = iter_chain
        self.condition = condition

    def to_python(self, state):

        iter_chain = utils.to_python(state, self.iter_chain)
        expr = self.expr.to_python(state)
        condition = [self.condition.to_python(
            state)] if self.condition != None else []

        iter_chain[-1].ifs = condition
        return ast.ListComp(elt=expr, generators=iter_chain)


class SetlIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression

    def to_python(self, state):
        [assignable, expression] = utils.to_python(
            state, [self.assignable, self.expression])
        return ast.comprehension(target=assignable, iter=expression, ifs=[], is_async=0)


class BooleanEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right)

    def to_python(self, state):
        [left_cond, right_cond] = utils.to_python(
            state, [self.left, self.right])
        left = utils.call_function("bool", [left_cond])
        right = utils.call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.Eq()], comparators=[right])


class BooleanNotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right)

    def to_python(self, state):
        [left_cond, right_cond] = utils.to_python(
            state, [self.left, self.right])
        left = utils.call_function("bool", [left_cond])
        right = utils.call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.NotEq()], comparators=[right])


class Implication(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right)

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        not_left = ast.UnaryOp(op=ast.Not(), operand=left)
        return ast.Compare(left=not_left, ops=[ast.Or()], comparators=[right])


class SetListConstructor:
    def __init__(self, collection):
        self.collection = collection

    def to_python(self, state):
        # TODO use own sets
        if self.collection == None:
            return utils.call_function("set", [])
        else:
            collection = self.collection.to_python(state)
            if isinstance(self.collection, types.Range):
                return utils.call_function("set", [collection.args[0]])
            elif isinstance(self.collection, SetlIteration):
                return ast.SetComp(elt=collection.elt, generators=collection.generators)
            else:
                return ast.Set(elts=collection.elts)
