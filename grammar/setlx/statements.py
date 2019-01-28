import grammar.python.statements as py_stmnt
import grammar.python.types as py_type
import grammar.python.block as py_block
from grammar.setlx.types import WithLevel
import grammar.setlx.utils as utils



class InfixOperator:
    def __init__(self, left, right, py_target_type):
        self.left = left
        self.right = right
        self.py_target_type = py_target_type

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        return (self.py_target_type)(left, right)


class Assignment(InfixOperator):
    def __init__(self, assignable, right_hand_side, target_type=py_stmnt.Assignment):
        InfixOperator.__init__(self,assignable, right_hand_side, target_type)


class SumAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(
            self, assignable, right_hand_side, py_stmnt.SumAssignment)


class DifferenceAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmnt.DifferenceAssignment)


class ProductAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmnt.ProductAssignment)


class QuotientAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmnt.QuotientAssignment)


class IntegerDivisionAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmnt.IntegerDivisionAssignment)


class ModuloAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmnt.ModuloAssignment)


class Factorial:
    def __init__(self, expr):
        self.expr = expr

    def to_python(self,state):
        expr = self.expr.to_python(state)
        return utils.call_function("factorial",[expr])


class FunctionCall:
    def __init__(self, params, expression):
        # maby later Call.__init__(self, None)
        self.params = params
        self.expression = expression
        self.callable = None

    def to_python(self, state):
        # TODO expression (unpack param)
        params = [p.to_python(state) for p in self.params]
        return py_stmnt.FunctionCall(self.callable.to_python(state), params)


class Call:
    def __init__(self, callable):
        self.callable = callable


class PrefixOperator:
    def __init__(self, expr, py_target_type):
        self.expr = expr
        self.py_target_type = py_target_type

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return (self.py_target_type)(expr)


class Equal(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Equal)


class GreaterThan(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.GreaterThan)


class NotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.NotEqual)


class Disjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Disjunction)


class Conjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Conjunction)


class Not(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, py_stmnt.Not)


class Difference(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Difference)


class Product(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmnt.Product)


class IfThen:
    def __init__(self, if_list=[]):
        self.if_list = if_list

    def to_python(self, state):
        if_list = [i.to_python(state) for i in self.if_list]
        return py_stmnt.IfThen(if_list)


class IfThenBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        return py_stmnt.IfThenBranch(condition, block)


class IfThenElseIfBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        [condition, block] = utils.to_python(
            state, [self.condition, self.block])
        return py_stmnt.IfThenElseIfBranch(condition, block)


class IfThenElseBranch:
    def __init__(self, block):
        self.block = block

    def to_python(self, state):
        block = self.block.to_python(state)
        return py_stmnt.IfThenElseBranch(block)


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
        return py_stmnt.Equal(left, right)


class BooleanNotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, None)

    def to_python(self, state):
        [left_cond, right_cond] = utils.to_python(
            state, [self.left, self.right])
        left = utils.call_function("bool", [left_cond])
        right = utils.call_function("bool", [right_cond])
        return py_stmnt.NotEqual(left, right)


class Implication(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, None)

    def to_python(self, state):
        [left, right] = utils.to_python(state, [self.left, self.right])
        return py_stmnt.Disjunction(py_stmnt.Not(left), right)
