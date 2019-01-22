class Assignment:
    def __init__(self, assignable, rightHandSide, operator="="):
        self.assignable = assignable
        self.rightHandSide = rightHandSide
        self.operator = operator

    def to_code(self, indent=0):
        return f"{self.assignable.to_code(indent)} {self.operator} {self.rightHandSide.to_code(indent)}"


class SumAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "+=")


class DifferenceAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "-=")


class ProductAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "*=")


class QuotientAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "/=")


class IntegerDivisionAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "//=")


class ModuloAssignment(Assignment):
    def __init__(self, assignable, rightHandSide):
        Assignment.__init__(self, assignable, rightHandSide, "%=")


class Factorial:
    def __init__(self, expr):
        self.expr = expr


class FunctionCall:
    def __init__(self, callable, params):
        self.callable = callable
        self.params = params

    def to_code(self, indent=0):
        params = [p.to_code(indent) for p in self.params]
        return f"{self.callable.to_code(indent)}({', '.join(params)})"


class Call:
    def __init__(self, callable):
        self.callable = callable


class InfixOperator:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def to_code(self, indent=0):
        left = self.left.to_code(indent)
        right = self.right.to_code(indent)
        return f"({left} {self.operator} {right})"


class PrefixOperator:
    def __init__(self, expr, operator):
        self.expr = expr
        self.operator = operator

    def to_code(self, indent=0):
        expr = self.expr.to_code(indent)
        return f"{self.operator}({expr})"


class Equal(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, "==")


class GreaterThan(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, ">")


class NotEqual(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, "!=")


class Disjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, "or")


class Conjunction(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, "and")


class Not(PrefixOperator):
    def __init__(self, expr):
        PrefixOperator.__init__(self, expr, "not")


class Difference(InfixOperator):
    def __init__(self, left, right):
        InfixOperator.__init__(self, left, right, "-")


class IfThen:
    def __init__(self, if_list=[]):
        self.if_list = if_list

    def to_code(self, indent=0):
        if_list = [i.to_code(indent) for i in self.if_list]
        return "\n".join(if_list)


class IfThenBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_code(self, indent=0):
        condition = self.condition.to_code(indent)
        block = self.block.to_code(indent+1)
        return f"if {condition}:\n{block}"


class IfThenElseIfBranch:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_code(self, indent=0):
        condition = self.condition.to_code(indent)
        block = self.block.to_code(indent+1)
        return f"elif {condition}:\n{block}"


class IfThenElseBranch:
    def __init__(self, block):
        self.block = block

    def to_code(self, indent=0):
        block = self.block.to_code(indent+1)
        return f"else:\n{block}"


class Condition:
    def __init__(self, expression):
        self.expression = expression

    def to_code(self, indent=0):
        return self.expression.to_code(indent)


class While:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def to_code(self, indent=0):
        condition = self.condition.to_code(indent)
        block = self.block.to_code(indent+1)
        return f"while {condition}:\n{block}"


class DoWhile:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class Backtrack:
    pass


class Break:
    def to_code(self, indent=0):
        return "break"


class Continue:
    def to_code(self, indent=0):
        return "continue"


class Exit:
    pass


class Return:
    def __init__(self, expression):
        self.expression = expression

    def to_code(self, indent=0):
        expression = self.expression.to_code(indent)
        return f"return {expression}"


class For:
    def __init__(self, iterator, block):
        self.iterator = iterator
        self.block = block

    def to_code(self, indent=0):
        iterator = self.iterator.to_code(indent)
        block = self.block.to_code(indent+1)
        return f"for {iterator}:\n{block}"


class PyIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression

    def to_code(self, indent=0):
        assignable = self.assignable.to_code(indent)
        expression = self.expression.to_code(indent)
        return f"{assignable} in {expression}"


class SetlIterator:
    def __init__(self, assignable, expression):
        self.assignable = assignable
        self.expression = expression


class Function:
    def __init__(self, id, params, block):
        self.params = params
        self.block = block
        self.id = id

    def to_code(self, indent=0):
        params = [p.to_code(indent) for p in self.params]
        block = self.block.to_code(indent+1)
        return f"def {self.id}({', '.join(params)}):\n{block}"
