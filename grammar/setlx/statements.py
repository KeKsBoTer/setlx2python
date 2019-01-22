import grammar.python.statements as py_stmt
import grammar.python.types as py_type
import grammar.python.block as py_block


class Assignment:
    def __init__(self, assignable, right_hand_side, target_type=py_stmt.Assignment):
        self.assignable = assignable
        self.right_hand_side = right_hand_side
        self.target_type = target_type

    def to_python(self, state):
        assignable = self.assignable.to_python(state)
        rhs = self.right_hand_side.to_python(state)
        return (self.target_type)(assignable, rhs)


class SumAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(
            self, assignable, right_hand_side, py_stmt.SumAssignment)


class DifferenceAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmt.DifferenceAssignment)


class ProductAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmt.ProductAssignment)


class QuotientAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmt.QuotientAssignment)


class IntegerDivisionAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmt.IntegerDivisionAssignment)


class ModuloAssignment(Assignment):
    def __init__(self, assignable, right_hand_side):
        Assignment.__init__(self, assignable, right_hand_side,
                            py_stmt.ModuloAssignment)


class Factorial:
    def __init__(self, expr):
        self.expr = expr


class FunctionCall:
    def __init__(self, params, expression):
        # maby later Call.__init__(self, None)
        self.params = params
        self.expression = expression
        self.callable = None

    def to_python(self, state):
        # TODO expression (unpack param)
        params = [p.to_python(state) for p in self.params]
        return py_stmt.FunctionCall(self.callable.to_python(state), params)


class Call:
    def __init__(self, callable):
        self.callable = callable


class InfixOperator:
    def __init__(self, left, right, py_target_type):
        self.left = left
        self.right = right
        self.py_target_type = py_target_type

    def to_python(self, state):
        left = self.left.to_python(state)
        right = self.right.to_python(state)
        return (self.py_target_type)(left, right)


class PrefixOperator:
    def __init__(self, expr, py_target_type):
        self.expr = expr
        self.py_target_type = py_target_type

    def to_python(self, state):
        expr = self.expr.to_python(state)
        return (self.py_target_type)(expr)


class Equal(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.Equal)


class GreaterThan(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.GreaterThan)


class NotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.NotEqual)


class Disjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.Disjunction)


class Conjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.Conjunction)


class Not(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, py_stmt.Not)


class Difference(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, py_stmt.Difference)


class IfThen:
    def __init__(self, if_list=[]):
        self.if_list = if_list

    def to_python(self, state):
        if_list = [i.to_python(state) for i in self.if_list]
        return py_stmt.IfThen(if_list)


class IfThenBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        condition = self.condition.to_python(state)
        block = self.block.to_python(state)
        return py_stmt.IfThenBranch(condition, block)


class IfThenElseIfBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        condition = self.condition.to_python(state)
        block = self.block.to_python(state)
        return py_stmt.IfThenElseIfBranch(condition, block)


class IfThenElseBranch:
    def __init__(self, block):
        self.block = block

    def to_python(self, state):
        block = self.block.to_python(state)
        return py_stmt.IfThenElseBranch(block)


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
        condition = self.condition.to_python(state)
        block = self.block.to_python(state)
        return py_stmt.While(condition, block)


class DoWhile:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self, state):
        condition = self.condition.to_python(state)
        block = self.block.to_python(state)
        # see tests/dowhile.py
        break_block = py_block.Block([py_stmt.Break()])
        negate = py_stmt.Not(condition)
        if_break = py_stmt.IfThen([py_stmt.IfThenBranch(negate, break_block)])
        block.stmnts.append(if_break)
        return py_stmt.While(py_type.PyTrue(), block)


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
        return py_stmt.Return(expression)


class For:
    def __init__(self, iteratorChain, condition, block):
        self.iteratorChain = iteratorChain
        self.condition = condition
        self.block = block

    def to_python(self, state):
        # see tests/for.py
        if len(self.iteratorChain) > 1:
            raise "more than one iterator chain in for loop is not supported yet"
        block = self.block.to_python(state)
        iterator = self.iteratorChain[0].to_python(state)
        # add condition as if statement in branch
        if self.condition != None:
            condition = self.condition.to_python(state)
            if_stmt = py_stmt.IfThen([py_stmt.IfThenBranch(condition, block)])
            block = py_block.Block([if_stmt])
        return py_stmt.For(iterator, block)


class SetlIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression

    def to_python(self, state):
        assignable = self.assignable.to_python(state)
        expression = self.expression.to_python(state)
        return py_stmt.PyIterator(assignable, expression)


class Procedure:
    def __init__(self, params, block, name=None):
        self.params = params
        self.block = block
        self.name = name

    def to_python(self, state):
        params = [p.to_python(state) for p in self.params]
        block = self.block.to_python(state)

        if self.name == None:
            proc_name = f"procedure_{state.procedure_counter}"

            state.before_stmnts += [py_stmt.Function(proc_name, params, block)]

            state.procedure_counter += 1
            return py_type.Variable(proc_name)
        else:
            return py_stmt.Function(self.name, params, block)
