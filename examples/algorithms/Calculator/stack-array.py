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
        self.mStackElements = mStackElements[1:len(mStackElements) - 1]

    @staticmethod
    @setlx.procedure
    def top():
        assert len(mStackElements) > 0, 'top of empty stack'
        return mStackElements[len(mStackElements)]

    @staticmethod
    @setlx.procedure
    def isEmpty():
        return mStackElements == setlx.List()

    @staticmethod
    @setlx.procedure
    def f_str():
        copy = self
        result = convert(copy)
        dashes = '\\n'
        for i in setlx.Set(setlx._range(1, len(result))):
            dashes += '-'
        return dashes + '\\n' + result + dashes + '\\n'

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
    n = len(l)
    for i in setlx.List(setlx._range(n, 1, n - 1 - n)):
        result.push(l[i])
    return result

