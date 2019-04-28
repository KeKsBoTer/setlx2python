import setlx
setlx.load('string-compare.stlx')


class map:
    isEmpty = lambda self=None: self.mKey == None

    @staticmethod
    @setlx.procedure
    def find(k, self=None):
        if isEmpty():
            return
        elif self.mKey == k:
            return self.mValue
        elif mCmpFct(k, self.mKey):
            return self.mLeft.find(k)
        else:
            return self.mRight.find(k)

    @staticmethod
    @setlx.procedure
    def insert(k, v, self=None):
        if isEmpty():
            self.mKey = k
            self.mValue = v
            self.mLeft = map(mCmpFct)
            self.mRight = map(mCmpFct)
        elif self.mKey == k:
            self.mValue = v
        elif mCmpFct(k, self.mKey):
            self.mLeft.insert(k, v)
        else:
            self.mRight.insert(k, v)

    @staticmethod
    @setlx.procedure
    def delMin(self=None):
        if self.mLeft.isEmpty():
            return setlx.List([self.mRight, self.mKey, self.mValue])
        else:
            [ls, km, vm] = self.mLeft.delMin()
            self.mLeft = ls
            return setlx.List([self, km, vm])

    @staticmethod
    @setlx.procedure
    def delete(k, self=None):
        if isEmpty():
            return
        elif k == self.mKey:
            if self.mLeft.isEmpty():
                self.update(self.mRight)
            elif self.mRight.isEmpty():
                self.update(self.mLeft)
            else:
                [rs, km, vm] = self.mRight.delMin()
                [self.mKey, self.mValue, self.mRight] = setlx.List([km, vm, rs])
        elif mCmpFct(k, self.mKey):
            self.mLeft.delete(k)
        else:
            self.mRight.delete(k)

    @staticmethod
    @setlx.procedure
    def update(t, self=None):
        self.mKey = t.mKey
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
    f_str = lambda self=None: self.toString(0)

    @staticmethod
    @setlx.procedure
    def toString(n, self=None):
        if isEmpty():
            return ' ' * n + 'Nil'
        else:
            return self.mLeft.toString(n + 4) + '\\n' + ' ' * n + '<' + self.mKey + ' |-> ' + self.mValue + '>\\n' + self.mRight.toString(n + 4)

    @setlx.procedure
    def __init__(self, cmp):
        self.toString = setlx.to_method(self, map.toString)
        self.f_str = setlx.to_method(self, map.f_str)
        self.update = setlx.to_method(self, map.update)
        self.delete = setlx.to_method(self, map.delete)
        self.delMin = setlx.to_method(self, map.delMin)
        self.insert = setlx.to_method(self, map.insert)
        self.find = setlx.to_method(self, map.find)
        self.isEmpty = setlx.to_method(self, map.isEmpty)
        self.mKey = mKey = None
        self.mValue = mValue = None
        self.mLeft = mLeft = None
        self.mRight = mRight = None
        self.mCmpFct = mCmpFct = setlx.copy(cmp)


@setlx.procedure
def demo(cmp):
    m = map(cmp)
    m.insert('anton', 123)
    m.insert('hugo', 345)
    m.insert('gustav', 789)
    m.insert('jens', 234)
    m.insert('hubert', 432)
    m.insert('andre', 342)
    m.insert('philipp', 342)
    m.insert('rene', 345)
    setlx.print(f'\\n{m}\\n')
    setlx.print(f'm.find(\\"anton\\" ) = {m.find(\'anton\')}')
    setlx.print(f'm.find(\\"hugo\\"  ) = {m.find(\'hugo\')}')
    setlx.print(f'm.find(\\"gustav\\") = {m.find(\'gustav\')}')
    setlx.print(f'm.find(\\"jens\\"  ) = {m.find(\'jens\')}')
    m.delete('philipp')
    setlx.print(f'\\n{m}\\n')
    setlx.print(f'm.find(\\"anton\\" ) = {m.find(\'anton\')}')
    setlx.print(f'm.find(\\"hugo\\"  ) = {m.find(\'hugo\')}')
    setlx.print(f'm.find(\\"gustav\\") = {m.find(\'gustav\')}')
    setlx.print(f'm.find(\\"jens\\"  ) = {m.find(\'jens\')}')
    return m


demo(lessThan)

