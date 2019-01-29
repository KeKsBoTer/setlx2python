import grammar.python.statements as py_stmnt
import grammar.python.types as py_type
import grammar.python.block as py_block
from grammar.setlx.types import WithLevel
import grammar.setlx.utils as utils
from grammar.setlx.block import Block
import ast


class InfixOperator:
    def __init__(self, left, right, py_target_type):
        self.left = left
        self.right = right
        self.py_target_type = py_target_type

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        # return (self.py_target_type)(left, right)
        return ast.Assign([left], right)


class Assignment:
    def __init__(self, assignable, right_hand_side):
        self.assignable = assignable
        self.right_hand_side = right_hand_side

    def to_python(self, state):
        [left, right] = utils.to_python(
            state, [self.assignable, self.right_hand_side])
        # return (self.py_target_type)(left, right)
        return ast.Assign([left], right)


class AssignmentOther:
    def __init__(self, assignable, right_hand_side, operator):
        self.assignable = assignable
        self.right_hand_side = right_hand_side
        self.operator = operator

    def to_python(self, state):
        [target, rhs] = utils.to_python(
            state, [self.assignable, self.right_hand_side])
        return ast.AugAssign(target, self.operator, rhs)


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


class Call:
    def __init__(self, callable):
        self.callable = callable


class PrefixOperator:
    def __init__(self, expr, py_target_type):
        self.expr = expr
        self.py_target_type = py_target_type

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return utils.call_function(self.py_target_type, [expr])


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


class NotEqual(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.NotEq())


class Disjunction(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.Or())


class Conjunction(Compare):
    def __init__(self, left, right):
        Compare.__init__(self, left, right, ast.And())


class Not(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, "not")


class Difference(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Difference)


class Product(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Product)


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
        return py_stmnt.While(condition, block)


class DoWhile:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        # see tests/dowhile.py
        break_block = py_block.Block([py_stmnt.Break()])
        negate = py_stmnt.Not(condition)
        if_break = py_stmnt.IfThen(
            [py_stmnt.IfThenBranch(negate, break_block)])
        block.stmnts.append(if_break)
        return py_stmnt.While(py_type.PyTrue(), block)


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
        return py_stmnt.Return(expression)


class For:
    def __init__(self, iteratorChain, condition, block):
        self.iteratorChain = iteratorChain
        self.condition = condition
        self.block = block

    def to_python(self, state):
        block = self.block.to_python(state)
        if len(self.iteratorChain) > 1:
            iterator = utils.iterator_from_chain(state, self.iteratorChain)
        else:
            iterator = self.iteratorChain[0].to_python(state)
        # add condition as if statement in branch
        if self.condition != None:
            condition = self.condition.to_python(state)
            if_stmt = py_stmnt.IfThen(
                [py_stmnt.IfThenBranch(condition, block)])
            block = py_block.Block([if_stmt])
        return py_stmnt.For(iterator, block)


class SetlIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression

    def to_python(self, state):
        [assignable, expression] = utils.to_python(
            state, [self.assignable, self.expression])
        return py_stmnt.PyIterator(assignable, expression)


def deep_copy_param(param, state):
    state.imports.add("copy", "deepcopy")
    call = py_stmnt.FunctionCall(py_type.Variable(
        "deepcopy"), [py_type.Parameter(param.id)])
    return py_stmnt.Assignment(py_type.Variable(param.id), call)


class Procedure:
    def __init__(self, params, block, name=None):
        self.params = params
        self.block = block
        self.name = name

    def to_python(self, state):
        params = [p.to_python(state) for p in self.params]
        block = self.block.to_python(state)
        deepcopies = [deep_copy_param(p, state) for p in params]
        block.stmnts = deepcopies + block.stmnts

        if self.name == None:
            # TODO find better naming
            proc_name = f"procedure_{state.level}_{state.procedure_counter}"

            state.before_stmnts.append(
                WithLevel(state.level, py_stmnt.Function(proc_name, params, block)))

            state.procedure_counter += 1
            return py_type.Variable(proc_name)
        else:
            return py_stmnt.Function(self.name, params, block)


class CollectionAccess:
    def __init__(self, params):
        self.params = params
        self.callable = None

    def to_python(self, state):
        callable = self.callable.to_python(
            state) if self.callable != None else None
        params = [py_stmnt.Difference(p.to_python(
            state), py_type.PyFraction(1, 1)) for p in self.params]
        return py_stmnt.CollectionAccess(params, callable)


class SetlIteration:
    def __init__(self, expr, iter_chain, condition):
        self.expr = expr
        self.iter_chain = iter_chain
        self.condition = condition

    def to_python(self, state):
        if len(self.iter_chain) > 1:
            iterator = utils.iterator_from_chain(state, self.iter_chain)
        else:
            iterator = self.iter_chain[0].to_python(state)
        expr = self.expr.to_python(state)
        condition = self.condition.to_python(
            state) if self.condition != None else None
        return py_stmnt.Iteration(expr, iterator, condition)


class BooleanEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, None)

    def to_python(self, state):
        [left_cond, right_cond] = utils.to_python(
            state, [self.left, self.right])
        left = utils.call_function("bool", [left_cond])
        right = utils.call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.Eq()], comparators=[right])


class BooleanNotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, None)

    def to_python(self, state):
        [left_cond, right_cond] = utils.to_python(
            state, [self.left, self.right])
        left = utils.call_function("bool", [left_cond])
        right = utils.call_function("bool", [right_cond])
        return ast.Compare(left=left, ops=[ast.NotEq()], comparators=[right])


class Implication(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, None)

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        not_left = utils.call_function("not", [left])
        return ast.Compare(left=not_left, ops=[ast.Or()], comparators=[right])
