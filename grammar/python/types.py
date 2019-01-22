from fractions import Fraction


class Variable:
    def __init__(self, id):
        self.id = id

    def to_code(self, indent=0):
        return self.id


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
        return f"None"


class Parameter:
    def __init__(self, id, default=None):
        self.id = id
        self.default = default
