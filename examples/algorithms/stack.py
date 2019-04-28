import setlx


class stack:

    @staticmethod
    @setlx.procedure
    def push(e, self=None):
        self.mStackElements += setlx.List([e])

    @staticmethod
    @setlx.procedure
    def pop(self=None):
        assert len(self.mStackElements) > 0, 'popping empty stack'
        self.mStackElements = self.mStackElements[1:-2]

    @staticmethod
    @setlx.procedure
    def top(self=None):
        assert len(self.mStackElements) > 0, 'top of empty stack'
        return self.mStackElements[-1]

    @staticmethod
    @setlx.procedure
    def isEmpty(self=None):
        return self.mStackElements == setlx.List()

    @staticmethod
    @setlx.procedure
    def f_str(self=None):
        result = self.convert(self)
        dashes = '-' * len(result)
        return setlx.join(setlx.List([dashes, result, dashes]), '\\n')

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
    for i in setlx.List(setlx._range(1, len(l))):
        result.push(l[-i])
    return result


s = createStack(setlx.List(setlx._range(1, 10)))
setlx.print(s)
while not s.isEmpty():
    t = s.top()
    setlx.print(t)
    s.pop()
    setlx.print(s, '\\n')

