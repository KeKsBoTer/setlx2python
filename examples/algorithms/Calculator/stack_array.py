import setlx


class stack(setlx.SetlXClass):

    @staticmethod
    def push(e, self=None):
        [e] = setlx.copy([e])
        self.mStackElements += setlx.List([e])

    @staticmethod
    def pop(self=None):
        assert len(self.mStackElements) > 0, 'popping empty stack'
        self.mStackElements = self.mStackElements[1:len(self.mStackElements) - 1]

    @staticmethod
    def top(self=None):
        assert len(self.mStackElements) > 0, 'top of empty stack'
        return self.mStackElements[len(self.mStackElements)]

    @staticmethod
    def isEmpty(self=None):
        return self.mStackElements == setlx.List()

    @staticmethod
    def f_str(self=None):
        copy = setlx.copy(self)
        result = self.convert(copy)
        dashes = '\n'
        for i in setlx.Set(setlx._range(1, len(result))):
            dashes += '-'
        return dashes + '\n' + result + dashes + '\n'

    @staticmethod
    def convert(s, self=None):
        [s] = setlx.copy([s])
        if s.isEmpty():
            return '|'
        top = s.top()
        s.pop()
        return self.convert(s) + ' ' + top + ' |'

    def __init__(self):
        self.convert = setlx.to_method(self, stack.convert, True)
        self.f_str = setlx.to_method(self, stack.f_str, True)
        self.isEmpty = setlx.to_method(self, stack.isEmpty, True)
        self.top = setlx.to_method(self, stack.top, True)
        self.pop = setlx.to_method(self, stack.pop, True)
        self.push = setlx.to_method(self, stack.push, True)
        self.mStackElements = setlx.List()


def createStack(l):
    [l] = setlx.copy([l])
    result = stack()
    n = len(l)
    for i in setlx.List(setlx._range(n, 1, n - 1 - n)):
        result.push(l[i])
    return result
