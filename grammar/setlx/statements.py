import grammar.python.statements as py_stmt


class Assignment:
    def __init__(self, assignable, right_hand_side, target_type=py_stmt.Assignment):
        self.assignable = assignable
        self.right_hand_side = right_hand_side
        self.target_type = target_type

    def to_python(self):
        assignable = self.assignable.to_python()
        rhs = self.right_hand_side.to_python()
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

    def to_python(self):
        # TODO expression (unpack param)
        params = [p.to_python() for p in self.params]
        return py_stmt.FunctionCall(self.callable.to_python(), params)


class Call:
    def __init__(self, callable):
        self.callable = callable


class InfixOperator:
    def __init__(self, left, right, py_target_type):
        self.left = left
        self.right = right
        self.py_target_type = py_target_type

    def to_python(self):
        left = self.left.to_python()
        right = self.right.to_python()
        return (self.py_target_type)(left, right)


class PrefixOperator:
    def __init__(self, expr, py_target_type):
        self.expr = expr
        self.py_target_type = py_target_type

    def to_python(self):
        expr = self.expr.to_python()
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

    def to_python(self):
        if_list = [i.to_python() for i in self.if_list]
        return py_stmt.IfThen(if_list)


class IfThenBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self):
        return py_stmt.IfThenBranch(self.condition,self.block)


class IfThenElseIfBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_python(self):
        return py_stmt.IfThenElseIfBranch(self.condition,self.block)


class IfThenElseBranch:
    def __init__(self, block):
        self.block = block

    def to_python(self):
        return py_stmt.IfThenElseBranch(self.block)


class Condition:
    def __init__(self, expression):
        self.expression = expression


class While:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class DoWhile:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


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


class For:
    def __init__(self, iteratorChain, condition, block):
        self.iteratorChain = iteratorChain
        self.condition = condition
        self.block = block


class SetlIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression


class Procedure:
    def __init__(self, params, block):
        self.params = params
        self.block = block
