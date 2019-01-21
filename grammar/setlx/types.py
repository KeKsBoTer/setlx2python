from fractions import Fraction

class AssignableVariable:
    def __init__(self,id):
        self.id = id

class SetlXFraction(Fraction):
    pass

class Variable:
    def __init__(self, id):
        self.id = id

class SetlXString:
    def __init__(self, value):
        if value.startswith('"') and value.endswith('"'):
            self.value = value[1:-1]
        else:
            self.value = value


class SetlXLiteral:
    def __init__(self, value):
        if value.startswith("'") and value.endswith("'"):
            self.value = value[1:-1]
        else:
            self.value = value
