import setlx


class stack:

    @staticmethod
    @setlx.procedure
    def push(e):
        self.mStackElements += setlx.List([e])

    @staticmethod
    @setlx.procedure
    def pop():
        assert len(mStackElements) > 0, 'popping empty stack'
        self.mStackElements = mStackElements[1:-2]

    @staticmethod
    @setlx.procedure
    def top():
        assert len(mStackElements) > 0, 'top of empty stack'
        return mStackElements[-1]

    @staticmethod
    @setlx.procedure
    def isEmpty():
        return mStackElements == setlx.List()

    @staticmethod
    @setlx.procedure
    def f_str():
        result = convert(self)
        dashes = '-' * len(result)
        return setlx.join(setlx.List([dashes, result, dashes]), '\\n')

    @staticmethod
    @setlx.procedure
    def convert(s):
        if s.isEmpty():
            return '|'
        top = s.top()
        s.pop()
        return convert(s) + ' ' + top + ' |'

    @setlx.procedure
    def __init__(self):
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

