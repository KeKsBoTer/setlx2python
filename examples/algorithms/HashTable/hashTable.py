import setlx


class hashTable(setlx.SetlXClass):
    sOrd = setlx.Set([setlx.List([setlx.char(i), i]) for i in setlx.List(setlx._range(0, 127))])
    sPrimes = setlx.List([3, 7, 13, 31, 61, 127, 251, 509, 1021, 2039, 4093, 8191, 16381, 32749, 65521, 131071, 262139, 524287, 1048573, 2097143, 4194301, 8388593, 16777213, 33554393, 67108859, 134217689, 268435399, 536870909, 1073741789, 2147483647])

    @staticmethod
    def hashCode(s, self=None):
        [s] = setlx.copy([s])
        return self.hashCodeAux(s) + 1

    @staticmethod
    def hashCodeAux(s, self=None):
        [s] = setlx.copy([s])
        if s == '':
            return 0
        return (sOrd[s[1]] + 128 * self.hashCodeAux(s[2:])) % self.mSize

    @staticmethod
    def find(key, self=None):
        [key] = setlx.copy([key])
        index = self.hashCode(key)
        aList = self.mArray[index]
        return aList[key]

    @staticmethod
    def insert(key, value, self=None):
        [key, value] = setlx.copy([key, value])
        if self.mEntries > self.mSize * self.mAlpha:
            self.rehash()
        index = self.hashCode(key)
        aList = self.mArray[index]
        oldSz = len(aList)
        aList[key] = setlx.copy(value)
        newSz = len(aList)
        self.mArray[index] = setlx.copy(aList)
        if newSz > oldSz:
            self.mEntries += 1

    @staticmethod
    def rehash(self=None):
        prime = setlx.min(setlx.Set([p for p in sPrimes if p * self.mAlpha > self.mEntries]))
        bigMap = hashTable(prime)
        for aList in self.mArray:
            for [k, v] in aList:
                bigMap.insert(k, v)
        self.mSize = setlx.copy(prime)
        self.mArray = bigMap.mArray

    @staticmethod
    def delete(key, self=None):
        [key] = setlx.copy([key])
        index = self.hashCode(key)
        aList = self.mArray[index]
        oldSz = len(aList)
        aList[key] = None
        newSz = len(aList)
        self.mArray[index] = setlx.copy(aList)
        if newSz < oldSz:
            self.mEntries -= 1

    @staticmethod
    def f_str(self=None):
        result = ''
        for i in setlx.List(setlx._range(1, len(self.mArray))):
            result += f'{i}: {self.mArray[i]}\n            '
        return result

    def __init__(self, n):
        self.f_str = setlx.to_method(self, hashTable.f_str, True)
        self.delete = setlx.to_method(self, hashTable.delete, True)
        self.rehash = setlx.to_method(self, hashTable.rehash, True)
        self.insert = setlx.to_method(self, hashTable.insert, True)
        self.find = setlx.to_method(self, hashTable.find, True)
        self.hashCodeAux = setlx.to_method(self, hashTable.hashCodeAux, True)
        self.hashCode = setlx.to_method(self, hashTable.hashCode, True)
        [n] = setlx.copy([n])
        self.mSize = setlx.copy(n)
        self.mEntries = 0
        self.mArray = setlx.List([setlx.Set() for i in setlx.List(setlx._range(1, self.mSize))])
        self.mAlpha = 2


def demo():
    data = setlx.readFile('data.txt')
    m = hashTable(3)
    keySet = setlx.Set()
    for line in data:
        [k, v] = setlx.split(line, ':')
        keySet += setlx.Set([k])
        v = removeWS(v)
        setlx.print(f'insert({k}, {v})')
        m.insert(k, v)
        setlx.print(f"""
        {m}
        """)
    for k in keySet:
        setlx.print(f'delete({k})')
        m.delete(k)
        setlx.print(f"""
        {m}
        """)


def removeWS(s):
    [s] = setlx.copy([s])
    ws = setlx.Set([' ', '\t', '\n', '\\r', '\\v'])
    return setlx.sum(setlx.List([s[i] for i in setlx.List(setlx._range(1, len(s))) if s[i] not in ws]))


demo()
