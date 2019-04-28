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
            self.mHeight = 1
        elif self.mKey == k:
            self.mValue = v
        elif mCmpFct(k, self.mKey):
            self.mLeft.insert(k, v)
            self.restore()
        else:
            self.mRight.insert(k, v)
            self.restore()

    @staticmethod
    @setlx.procedure
    def delMin(self=None):
        if self.mLeft.isEmpty():
            return setlx.List([self.mRight, self.mKey, self.mValue])
        else:
            [ls, km, vm] = self.mLeft.delMin()
            self.mLeft = ls
            self.restore()
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
                self.restore()
        elif mCmpFct(k, self.mKey):
            self.mLeft.delete(k)
            self.restore()
        else:
            self.mRight.delete(k)
            self.restore()

    @staticmethod
    @setlx.procedure
    def update(t, self=None):
        self.mKey = t.mKey
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
        self.mHeight = t.mHeight

    @staticmethod
    @setlx.procedure
    def restore(self=None):
        if setlx.abs(self.mLeft.mHeight - self.mRight.mHeight) <= 1:
            self.restoreHeight()
            return
        if self.mLeft.mHeight > self.mRight.mHeight:
            [k1, v1, l1, r1] = setlx.List([self.mKey, self.mValue, self.mLeft, self.mRight])
            [k2, v2, l2, r2] = setlx.List([l1.mKey, l1.mValue, l1.mLeft, l1.mRight])
            if l2.mHeight >= r2.mHeight:
                self.setValues(k2, v2, l2, createNode(k1, v1, r2, r1, mCmpFct))
            else:
                [k3, v3, l3, r3] = setlx.List([r2.mKey, r2.mValue, r2.mLeft, r2.mRight])
                self.setValues(k3, v3, createNode(k2, v2, l2, l3, mCmpFct), createNode(k1, v1, r3, r1, mCmpFct))
        elif self.mRight.mHeight > self.mLeft.mHeight:
            [k1, v1, l1, r1] = setlx.List([self.mKey, self.mValue, self.mLeft, self.mRight])
            [k2, v2, l2, r2] = setlx.List([r1.mKey, r1.mValue, r1.mLeft, r1.mRight])
            if r2.mHeight >= l2.mHeight:
                self.setValues(k2, v2, createNode(k1, v1, l1, l2, mCmpFct), r2)
            else:
                [k3, v3, l3, r3] = setlx.List([l2.mKey, l2.mValue, l2.mLeft, l2.mRight])
                self.setValues(k3, v3, createNode(k1, v1, l1, l3, mCmpFct), createNode(k2, v2, r3, r2, mCmpFct))
        self.restoreHeight()

    @staticmethod
    @setlx.procedure
    def setValues(k, v, l, r, self=None):
        self.mKey = k
        self.mValue = v
        self.mLeft = l
        self.mRight = r

    @staticmethod
    @setlx.procedure
    def restoreHeight(self=None):
        self.mHeight = 1 + setlx.max(setlx.Set([self.mLeft.mHeight, self.mRight.mHeight]))
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
        self.restoreHeight = setlx.to_method(self, map.restoreHeight)
        self.setValues = setlx.to_method(self, map.setValues)
        self.restore = setlx.to_method(self, map.restore)
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
        self.mHeight = mHeight = 0
        self.mCmpFct = mCmpFct = setlx.copy(cmp)


@setlx.procedure
def createNode(key, value, left, right, cmp):
    node = map(cmp)
    node.mKey = key
    node.mValue = value
    node.mLeft = left
    node.mRight = right
    node.mCmpFct = cmp
    node.mHeight = 1 + setlx.max(setlx.Set([left.mHeight, right.mHeight]))
    return node


@setlx.procedure
def demo(cmp):
    data = setlx.readFile('data.txt')
    m = map(cmp)
    for line in data:
        [k, v] = setlx.split(line, ':')
        v = removeWS(v)
        setlx.print(f'insert({k}, {v})')
        m.insert(k, v)
    setlx.print(m)
    while True:
        k = setlx.read('zu loeschenden Schl�ssel eingeben: ')
        m.delete(k)
        setlx.print(m)


@setlx.procedure
def removeWS(s):
    ws = setlx.Set([' ', '\\t', '\\n', '\\r', '\\v'])
    return setlx.sum(setlx.List([s[i] for i in setlx.List(setlx._range(1, len(s))) if s[i] not in ws]))


demo(lessThan)

