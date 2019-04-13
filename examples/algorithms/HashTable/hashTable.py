import setlx


class hashTable:
    sOrd = setlx.Set([setlx.List([setlx.char(i), i]) for i in setlx.List(setlx._range(0, 127))])
    sPrimes = setlx.List([3, 7, 13, 31, 61, 127, 251, 509, 1021, 2039, 4093, 8191, 16381, 32749, 65521, 131071, 262139, 524287, 1048573, 2097143, 4194301, 8388593, 16777213, 33554393, 67108859, 134217689, 268435399, 536870909, 1073741789, 2147483647])

    @staticmethod
    @setlx.procedure
    def hashCode(s):
        return hashCodeAux(s) + 1

    @staticmethod
    @setlx.procedure
    def hashCodeAux(s):
        if s == '':
            return 0
        return (sOrd[s[1]] + 128 * hashCodeAux(s[2:])) % mSize

    @staticmethod
    @setlx.procedure
    def find(key):
        index = hashCode(key)
        aList = mArray[index]
        return aList[key]

    @staticmethod
    @setlx.procedure
    def insert(key, value):
        if mEntries > mSize * mAlpha:
            rehash()
        index = hashCode(key)
        aList = mArray[index]
        oldSz = len(aList)
        aList[key] = value
        newSz = len(aList)
        self.mArray[index] = aList
        if newSz > oldSz:
            self.mEntries += 1

    @staticmethod
    @setlx.procedure
    def rehash():
        prime = setlx.min(setlx.Set([p for p in sPrimes if p * mAlpha > mEntries]))
        bigMap = hashTable(prime)
        for aList in mArray:
            for [k, v] in aList:
                bigMap.insert(k, v)
        self.mSize = prime
        self.mArray = bigMap.mArray

    @staticmethod
    @setlx.procedure
    def delete(key):
        index = hashCode(key)
        aList = mArray[index]
        oldSz = len(aList)
        aList[key] = None
        newSz = len(aList)
        self.mArray[index] = aList
        if newSz < oldSz:
            self.mEntries -= 1

    @staticmethod
    @setlx.procedure
    def f_str():
        result = ''
        for i in setlx.List(setlx._range(1, len(mArray))):
            result += f'{i}: {mArray[i]}\\n'
        return result

    @setlx.procedure
    def __init__(self, n):
        self.mSize = mSize = n
        self.mEntries = mEntries = 0
        self.mArray = mArray = setlx.List([setlx.Set() for i in setlx.List(setlx._range(1, mSize))])
        self.mAlpha = mAlpha = 2


@setlx.procedure
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
        setlx.print(f'\\n{m}\\n')
    for k in keySet:
        setlx.print(f'delete({k})')
        m.delete(k)
        setlx.print(f'\\n{m}\\n')


@setlx.procedure
def removeWS(s):
    ws = setlx.Set([' ', '\\t', '\\n', '\\r', '\\v'])
    return setlx.sum(setlx.List([s[i] for i in setlx.List(setlx._range(1, len(s))) if s[i] not in ws]))


demo()

