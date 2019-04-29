import setlx
from string_compare import *


class map(setlx.SetlXClass):
    isEmpty = lambda self=None: self.mKey == None

    @staticmethod
    def find(k, self=None):
        [k] = setlx.copy([k])
        if self.isEmpty():
            return
        elif self.mKey == k:
            return self.mValue
        elif self.mCmpFct(k, self.mKey):
            return self.mLeft.find(k)
        else:
            return self.mRight.find(k)

    @staticmethod
    def insert(k, v, self=None):
        [k, v] = setlx.copy([k, v])
        if self.isEmpty():
            self.mKey = setlx.copy(k)
            self.mValue = setlx.copy(v)
            self.mLeft = map(self.mCmpFct)
            self.mRight = map(self.mCmpFct)
        elif self.mKey == k:
            self.mValue = setlx.copy(v)
        elif self.mCmpFct(k, self.mKey):
            self.mLeft.insert(k, v)
        else:
            self.mRight.insert(k, v)

    @staticmethod
    def delMin(self=None):
        if self.mLeft.isEmpty():
            return setlx.List([self.mRight, self.mKey, self.mValue])
        else:
            [ls, km, vm] = self.mLeft.delMin()
            self.mLeft = setlx.copy(ls)
            return setlx.List([self, km, vm])

    @staticmethod
    def delete(k, self=None):
        [k] = setlx.copy([k])
        if self.isEmpty():
            return
        elif k == self.mKey:
            if self.mLeft.isEmpty():
                self.update(self.mRight)
            elif self.mRight.isEmpty():
                self.update(self.mLeft)
            else:
                [rs, km, vm] = self.mRight.delMin()
                [self.mKey, self.mValue, self.mRight] = setlx.List([km, vm, rs])
        elif self.mCmpFct(k, self.mKey):
            self.mLeft.delete(k)
        else:
            self.mRight.delete(k)

    @staticmethod
    def update(t, self=None):
        [t] = setlx.copy([t])
        self.mKey = t.mKey
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
    f_str = lambda self=None: self.toString(0)

    @staticmethod
    def toString(n, self=None):
        [n] = setlx.copy([n])
        if self.isEmpty():
            return ' ' * n + 'Nil'
        else:
            return self.mLeft.toString(n + 4) + '\n' + ' ' * n + '<' + self.mKey + ' |-> ' + self.mValue + '>\n' + self.mRight.toString(n + 4)

    def __init__(self, cmp):
        self.toString = setlx.to_method(self, map.toString, True)
        self.f_str = setlx.to_method(self, map.f_str, True)
        self.update = setlx.to_method(self, map.update, True)
        self.delete = setlx.to_method(self, map.delete, True)
        self.delMin = setlx.to_method(self, map.delMin, True)
        self.insert = setlx.to_method(self, map.insert, True)
        self.find = setlx.to_method(self, map.find, True)
        self.isEmpty = setlx.to_method(self, map.isEmpty, True)
        [cmp] = setlx.copy([cmp])
        self.mKey = None
        self.mValue = None
        self.mLeft = None
        self.mRight = None
        self.mCmpFct = setlx.copy(cmp)


def demo(cmp):
    [cmp] = setlx.copy([cmp])
    m = map(cmp)
    m.insert('anton', 123)
    m.insert('hugo', 345)
    m.insert('gustav', 789)
    m.insert('jens', 234)
    m.insert('hubert', 432)
    m.insert('andre', 342)
    m.insert('philipp', 342)
    m.insert('rene', 345)
    setlx.print(f'\n    {m}\n    ')
    setlx.print(f'm.find(\\"anton\\" ) = {m.find(\'anton\')}')
    setlx.print(f'm.find(\\"hugo\\"  ) = {m.find(\'hugo\')}')
    setlx.print(f'm.find(\\"gustav\\") = {m.find(\'gustav\')}')
    setlx.print(f'm.find(\\"jens\\"  ) = {m.find(\'jens\')}')
    m.delete('philipp')
    setlx.print(f'\n    {m}\n    ')
    setlx.print(f'm.find(\\"anton\\" ) = {m.find(\'anton\')}')
    setlx.print(f'm.find(\\"hugo\\"  ) = {m.find(\'hugo\')}')
    setlx.print(f'm.find(\\"gustav\\") = {m.find(\'gustav\')}')
    setlx.print(f'm.find(\\"jens\\"  ) = {m.find(\'jens\')}')
    return m


demo(lessThan)
