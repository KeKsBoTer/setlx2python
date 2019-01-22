from fractions import Fraction
import grammar.python.types as py_type


class AssignableVariable:
    def __init__(self, id):
        self.id = id

    def to_python(self):
        return py_type.Variable(self.id)


class SetlXFraction(Fraction):
    def to_python(self):
        return py_type.PyFraction(self)


class Variable:
    def __init__(self, id):
        self.id = id
        
    def to_python(self):
        return py_type.Variable(self.id)


class SetlXString:
    def __init__(self, value):
        if value.startswith('"') and value.endswith('"'):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self):
        return py_type.String(self.value)


class SetlXLiteral:
    def __init__(self, value):
        if value.startswith("'") and value.endswith("'"):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self):
        return py_type.Literal(self.value)


class SetlXOm:

    def to_python(self):
        return py_type.PyNone()


class Parameter:
    def __init__(self, id, default=None):
        self.id = id
        self.default = default
