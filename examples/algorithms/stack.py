import setlx


class stack(setlx.SetlXClass):

    @staticmethod
    def push(e, self=None):
        [e] = setlx.copy([e])
        self.mStackElements += setlx.List([e])

    @staticmethod
    def pop(self=None):
        assert len(self.mStackElements) > 0, 'popping empty stack'
        self.mStackElements = self.mStackElements[1:-2]

    @staticmethod
    def top(self=None):
        assert len(self.mStackElements) > 0, 'top of empty stack'
        return self.mStackElements[-1]

    @staticmethod
    def isEmpty(self=None):
        return self.mStackElements == setlx.List()

    @staticmethod
    def f_str(self=None):
        result = self.convert(self)
        dashes = '-' * len(result)
        return setlx.join(setlx.List([dashes, result, dashes]), '\n')

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
    for i in setlx.List(setlx._range(1, len(l))):
        result.push(l[-i])
    return result


s = createStack(setlx.List(setlx._range(1, 10)))
setlx.print(s)
while not s.isEmpty():
    t = s.top()
    setlx.print(t)
    s.pop()
    setlx.print(s, '\n')
