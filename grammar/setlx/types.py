from fractions import Fraction
import grammar.python.types as py_type


class AssignableVariable:
    def __init__(self, id):
        self.id = id

    def to_python(self, state):
        return py_type.Variable(self.id)


class AssignableList:
    def __init__(self, assignables):
        self.assignables = assignables

    def to_python(self, state):
        assignables = [a.to_python(state) for a in self.assignables]
        return py_type.AssignableList(assignables)


class SetlXFraction(Fraction):
    def to_python(self, state):
        return py_type.PyFraction(self)


class Variable:
    def __init__(self, id):
        self.id = id

    def to_python(self, state):
        return py_type.Variable(self.id)


class SetlXString:
    def __init__(self, value):
        if value.startswith('"') and value.endswith('"'):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self, state):
        return py_type.String(self.value)


class SetlXLiteral:
    def __init__(self, value):
        if value.startswith("'") and value.endswith("'"):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self, state):
        return py_type.Literal(self.value)


class SetlXOm:
    def to_python(self, state):
        return py_type.PyNone()


class Parameter:
    def __init__(self, id, default=None):
        self.id = id
        self.default = default

    def to_python(self, state):
        default = self.default.to_python(
            state) if self.default != None else None
        return py_type.Parameter(self.id, default)


class SetlXTrue:
    def to_python(self, state):
        return py_type.PyTrue()


class SetlXFalse:
    def to_python(self, state):
        return py_type.PyFalse()


class SetlXList:
    def __init__(self, expr):
        self.expr = expr

    def to_python(self, state):
        expr = self.expr.to_python(state) if self.expr != None else None
        return py_type.PyList(expr)


class ExplicitList:
    def __init__(self, exprs):
        self.exprs = exprs

    def to_python(self, state):
        exprs = [e.to_python(state) for e in self.exprs]
        return py_type.ExplicitList(exprs)


class WithLevel:
    def __init__(self,level,code):
        self.code = code
        self.level = level

    def to_code(self,indent=0):
        return self.code.to_code(indent)
