import setlx
setlx.load('string-compare.stlx')


class map:
    isEmpty = lambda : mKey == None

    @staticmethod
    @setlx.procedure
    def find(k):
        if isEmpty():
            return
        elif mKey == k:
            return mValue
        elif mCmpFct(k, mKey):
            return mLeft.find(k)
        else:
            return mRight.find(k)

    @staticmethod
    @setlx.procedure
    def insert(k, v):
        if isEmpty():
            self.mKey = k
            self.mValue = v
            self.mLeft = map(mCmpFct)
            self.mRight = map(mCmpFct)
        elif mKey == k:
            self.mValue = v
        elif mCmpFct(k, mKey):
            mLeft.insert(k, v)
        else:
            mRight.insert(k, v)

    @staticmethod
    @setlx.procedure
    def delMin():
        if mLeft.isEmpty():
            return setlx.List([mRight, mKey, mValue])
        else:
            [ls, km, vm] = mLeft.delMin()
            self.mLeft = ls
            return setlx.List([self, km, vm])

    @staticmethod
    @setlx.procedure
    def delete(k):
        if isEmpty():
            return
        elif k == mKey:
            if mLeft.isEmpty():
                update(mRight)
            elif mRight.isEmpty():
                update(mLeft)
            else:
                [rs, km, vm] = mRight.delMin()
                [self.mKey, self.mValue, self.mRight] = setlx.List([km, vm, rs])
        elif mCmpFct(k, mKey):
            mLeft.delete(k)
        else:
            mRight.delete(k)

    @staticmethod
    @setlx.procedure
    def update(t):
        self.mKey = t.mKey
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
    f_str = lambda : toString(0)

    @staticmethod
    @setlx.procedure
    def toString(n):
        if isEmpty():
            return ' ' * n + 'Nil'
        else:
            return mLeft.toString(n + 4) + '\\n' + ' ' * n + '<' + mKey + ' |-> ' + mValue + '>\\n' + mRight.toString(n + 4)

    @setlx.procedure
    def __init__(self, cmp):
        self.mKey = mKey = None
        self.mValue = mValue = None
        self.mLeft = mLeft = None
        self.mRight = mRight = None
        self.mCmpFct = mCmpFct = cmp


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

