import setlx


class linkedList:

    @staticmethod
    @setlx.procedure
    def equals(rhs):
        if rhs == -1:
            return False
        return mData == rhs.mData and mNext == rhs.mNext

    @setlx.procedure
    def __init__(self, data, next):
        self.mData = mData = data
        self.mNext = mNext = next


class stack:

    @staticmethod
    @setlx.procedure
    def push(e):
        self.mPointer = linkedList(e, mPointer)

    @staticmethod
    @setlx.procedure
    def pop():
        assert mPointer != -1, 'popping empty stack'
        self.mPointer = mPointer.mNext

    @staticmethod
    @setlx.procedure
    def top():
        assert mPointer != -1, 'top of empty stack'
        return mPointer.mData

    @staticmethod
    @setlx.procedure
    def isEmpty():
        return mPointer == -1

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
        self.mPointer = mPointer = -1

