import setlx


class linkedList:

    @staticmethod
    @setlx.procedure
    def equals(rhs, self=None):
        if rhs == -1:
            return False
        return mData == rhs.mData and mNext == rhs.mNext

    @setlx.procedure
    def __init__(self, data, next):
        self.equals = setlx.to_method(self, linkedList.equals)
        self.mData = mData = setlx.copy(data)
        self.mNext = mNext = setlx.copy(next)


class stack:

    @staticmethod
    @setlx.procedure
    def push(e, self=None):
        self.mPointer = linkedList(e, self.mPointer)

    @staticmethod
    @setlx.procedure
    def pop(self=None):
        assert self.mPointer != -1, 'popping empty stack'
        self.mPointer = self.mPointer.mNext

    @staticmethod
    @setlx.procedure
    def top(self=None):
        assert self.mPointer != -1, 'top of empty stack'
        return self.mPointer.mData

    @staticmethod
    @setlx.procedure
    def isEmpty(self=None):
        return self.mPointer == -1

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
        self.mPointer = mPointer = -1

