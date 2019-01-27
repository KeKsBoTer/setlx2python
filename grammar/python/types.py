from fractions import Fraction
from grammar.python.statements import FunctionCall

class Variable:
    def __init__(self, id):
        self.id = id

    def to_code(self, indent=0):
        return self.id


class AssignableList:
    def __init__(self, assignables):
        self.assignables = assignables

    def to_code(self, indent=0):
        assignables = [a.to_code(indent) for a in self.assignables]
        return f"[{', '.join(assignables)}]"


class PyFraction(Fraction):

    def to_code(self, indent=0):
        if self.denominator != 1:
            return f"{self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}"


class String:
    def __init__(self, value):
        if value.startswith('"') and value.endswith('"'):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_code(self, indent=0):
        return f'"{self.value}"'


class Literal:
    def __init__(self, value):
        if value.startswith("'") and value.endswith("'"):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_code(self, indent=0):
        return f"'{self.value}'"


class PyNone:
    def to_code(self, indent=0):
        return "None"


class PyTrue:
    def to_code(self, indent=0):
        return "True"


class PyFalse:
    def to_code(self, indent=0):
        return "False"


class Parameter:
    def __init__(self, id, default=None):
        self.id = id
        self.default = default

    def to_code(self, indent=0):
        if self.default == None:
            return self.id
        else:
            default = self.default.to_code(indent)
            return f"{id} := {default}"


class PyList:
    def __init__(self, expr):
        self.expr = expr

    def to_code(self, indent=0):
        expr = self.expr.to_code(indent)if self.expr != None else ""
        if isinstance(self.expr,Range):
            return expr
        else:
            return f"[{expr}]"


class ExplicitList:
    def __init__(self, exprs):
        self.exprs = exprs

    def to_code(self, indent=0):
        exprs = [e.to_code(indent) for e in self.exprs]
        return ", ".join(exprs)


class ListRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_code(self, indent=0):
        start = self.start.to_code(indent) if self.start != None else 0
        end = self.end.to_code(indent) if self.end != None else 0
        return f"{start}:{end}"

class Range:
    def __init__(self,start,step,end):
        self.start = start
        self.step = step
        self.end = end

    def to_code(self,indent=0):
        #start = self.start.to_code(indent)
        #end = self.end.to_code(indent)
        if self.step != None:
            #step = self.step.to_code(indent) if self.step != None else None
            rangeCall = FunctionCall(Variable("range"),[self.start,self.end,self.step])
        else:
            rangeCall = FunctionCall(Variable("range"),[self.start,self.end])

        listCall = FunctionCall(Variable("list"),[rangeCall])
        return listCall.to_code(indent)
