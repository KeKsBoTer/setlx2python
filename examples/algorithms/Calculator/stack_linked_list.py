import setlx


class linkedList(setlx.SetlXClass):

    @staticmethod
    def equals(rhs, self=None):
        [rhs] = setlx.copy([rhs])
        if rhs == -1:
            return False
        return self.mData == rhs.mData and self.mNext == rhs.mNext

    def __init__(self, data, next):
        self.equals = setlx.to_method(self, linkedList.equals, True)
        [data, next] = setlx.copy([data, next])
        self.mData = setlx.copy(data)
        self.mNext = setlx.copy(next)


class stack(setlx.SetlXClass):

    @staticmethod
    def push(e, self=None):
        [e] = setlx.copy([e])
        self.mPointer = linkedList(e, self.mPointer)

    @staticmethod
    def pop(self=None):
        assert self.mPointer != -1, 'popping empty stack'
        self.mPointer = self.mPointer.mNext

    @staticmethod
    def top(self=None):
        assert self.mPointer != -1, 'top of empty stack'
        return self.mPointer.mData

    @staticmethod
    def isEmpty(self=None):
        return self.mPointer == -1

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
        self.mPointer = -1
