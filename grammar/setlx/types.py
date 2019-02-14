from fractions import Fraction
import grammar.setlx.utils as utils
import ast


class Variable:
    def __init__(self, id):
        self.id = id

    def to_python(self, state):
        id_str = self.id if self.id != "this" else "self"
        return ast.Name(id=id_str)


class AssignableList:
    def __init__(self, assignables):
        self.assignables = assignables

    def to_python(self, state):
        assignables = [a.to_python(state) for a in self.assignables]
        return ast.List(elts=assignables)


class SetlXFraction(Fraction):
    def to_python(self, state):
        return ast.Num(self.numerator)


class SetlXString:
    def __init__(self, value):
        if value.startswith('"') and value.endswith('"'):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self, state):
        return ast.Str(self.value)


class SetlXLiteral:
    def __init__(self, value):
        if value.startswith("'") and value.endswith("'"):
            self.value = value[1:-1]
        else:
            self.value = value

    def to_python(self, state):
        return ast.Str(s=self.value)


class SetlXOm:
    def to_python(self, state):
        return ast.NameConstant(None)


class Parameter:
    def __init__(self, id, default=None, read_write=False):
        self.id = id
        self.default = default
        self.read_write = read_write

    def to_python(self, state):
        return ast.arg(arg=self.id, annotation=None)


class ReadWriteParameter:
    def __init__(self, id):
        self.id = id

    def to_python(self, state):
        return ast.arg(arg=self.id, annotation=None)


class ListParameter:
    def __init__(self, id):
        self.id = id

    def to_python(self, state):
        raise "not reachable"


class SetlXTrue:
    def to_python(self, state):
        return utils.bool_true()


class SetlXFalse:
    def to_python(self, state):
        return utils.bool_false()


class SetlXList:
    def __init__(self, expr):
        self.expr = expr

    def to_python(self, state):
        if self.expr != None:
            return self.expr.to_python(state)
        else:
            return ast.List(elts=[])


class ExplicitList:
    def __init__(self, exprs):
        self.exprs = exprs

    def to_python(self, state):
        return ast.List(elts=[e.to_python(state) for e in self.exprs])


class WithLevel:
    def __init__(self, level, code):
        self.code = code
        self.level = level

    def to_python(self, state):
        return self.code


class ListRange:
    # range for list access
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_python(self, state):
        start = self.start.to_python(state) if self.start != None else None
        end = self.end.to_python(state) if self.end != None else None
        if start != None:
            start = ast.BinOp(left=start, op=ast.Sub(), right=ast.Num(1))
        return ast.Slice(lower=start, upper=end, step=None)


class Range:
    # range for creating lings
    def __init__(self, start, step, end):
        self.start = start
        self.step = step
        self.end = end

    def to_python(self, state):
        start = self.start.to_python(state)
        end = self.end.to_python(state)
        end_plus_one = ast.BinOp(left=end, op=ast.Add(), right=ast.Num(n=1))
        range_params = [start, end_plus_one]

        if self.step != None:
            step = ast.BinOp(left=self.step.to_python(
                state), op=ast.Sub(), right=start)
            range_params.append(step)

        range_call = utils.call_function("range", range_params)
        return utils.call_function("list", [range_call])
