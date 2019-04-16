﻿import setlx


class stack:

    @staticmethod
    @setlx.procedure
    def push(e, self=None):
        self.mStackElements += setlx.List([e])

    @staticmethod
    @setlx.procedure
    def pop(self=None):
        assert len(self.mStackElements) > 0, 'popping empty stack'
        self.mStackElements = self.mStackElements[1:len(self.mStackElements) - 1]

    @staticmethod
    @setlx.procedure
    def top(self=None):
        assert len(self.mStackElements) > 0, 'top of empty stack'
        return self.mStackElements[len(self.mStackElements)]

    @staticmethod
    @setlx.procedure
    def isEmpty(self=None):
        return self.mStackElements == setlx.List()

    @staticmethod
    @setlx.procedure
    def f_str(self=None):
        copy = setlx.copy(self)
        result = self.convert(copy)
        dashes = '\\n'
        for i in setlx.Set(setlx._range(1, len(result))):
            dashes += '-'
        return dashes + '\\n' + result + dashes + '\\n'

    @staticmethod
    @setlx.procedure
    def convert(s, self=None):
        if s.isEmpty():
            return '|'
        top = s.top()
        s.pop()
        return self.convert(s) + ' ' + top + ' |'

    @setlx.procedure
    def __init__(self):
        self.convert = setlx.to_method(self, stack.convert)
        self.f_str = setlx.to_method(self, stack.f_str)
        self.isEmpty = setlx.to_method(self, stack.isEmpty)
        self.top = setlx.to_method(self, stack.top)
        self.pop = setlx.to_method(self, stack.pop)
        self.push = setlx.to_method(self, stack.push)
        self.mStackElements = mStackElements = setlx.List()


@setlx.procedure
def createStack(l):
    result = stack()
    n = len(l)
    for i in setlx.List(setlx._range(n, 1, n - 1 - n)):
        result.push(l[i])
    return result

