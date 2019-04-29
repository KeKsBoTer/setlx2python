import setlx


class lzw(setlx.SetlXClass):

    @staticmethod
    def compress(s, self=None):
        [s] = setlx.copy([s])
        result = setlx.List()
        idx = 1
        while idx <= len(s):
            p = self.longestPrefix(s, idx)
            result[len(result) + 1] = self.mDictionary[s[idx:p]]
            self.mCodeSize += self.mBitNumber
            self.wPrint(f'{self.mDictionary[s[idx:p]]} codes {s[idx:p]}')
            if p < len(s):
                self.mDictionary[s[idx:p + 1]] = setlx.copy(self.mNextCode)
                self.wPrint(f'adding {s[idx:p + 1]} |-> {self.mNextCode}')
                self.mNextCode += 1
                self.incrementBitNumber()
            idx = p + 1
        return result

    @staticmethod
    def longestPrefix(s, i, self=None):
        [s, i] = setlx.copy([s, i])
        oldK = setlx.copy(i)
        k = i + 1
        while k <= len(s) and self.mDictionary[s[i:k]] != None:
            oldK = setlx.copy(k)
            k += 1
        return oldK

    @staticmethod
    def incrementBitNumber(self=None):
        if 2 ** self.mBitNumber <= self.mNextCode:
            self.mBitNumber += 1

    @staticmethod
    def uncompress(l, self=None):
        [l] = setlx.copy([l])
        result = ''
        idx = 1
        code = l[idx]
        old = self.mInverse[code]
        idx += 1
        self.wPrint(f'{code} codes {old}')
        while idx <= len(l):
            result += old
            code = l[idx]
            idx += 1
            next = self.mInverse[code]
            self.wPrint(f'{code} codes {next}')
            if next == None:
                next = old + old[1]
            self.mInverse[self.mNextCode] = old + next[1]
            self.wPrint(f'adding {self.mNextCode} |-> {(old + next[1])}')
            self.mNextCode += 1
            old = setlx.copy(next)
        result += old
        return result

    @staticmethod
    def wPrint(s, self=None):
        [s] = setlx.copy([s])
        if self.mWatch:
            setlx.print(s)

    def __init__(self, watch):
        self.wPrint = setlx.to_method(self, lzw.wPrint, True)
        self.uncompress = setlx.to_method(self, lzw.uncompress, True)
        self.incrementBitNumber = setlx.to_method(self, lzw.incrementBitNumber, True)
        self.longestPrefix = setlx.to_method(self, lzw.longestPrefix, True)
        self.compress = setlx.to_method(self, lzw.compress, True)
        [watch] = setlx.copy([watch])
        self.mDictionary = setlx.Set([setlx.List([setlx.char(i), i]) for i in setlx.List(setlx._range(0, 127))])
        self.mInverse = setlx.Set([setlx.List([i, setlx.char(i)]) for i in setlx.List(setlx._range(0, 127))])
        self.mNextCode = 128
        self.mBitNumber = 8
        self.mCodeSize = 0
        self.mWatch = setlx.copy(watch)


def demo(s, w):
    [s, w] = setlx.copy([s, w])
    if len(s) < 1000:
        setlx.print(f'now compressing \\"{s}\\"')
    compressor = lzw(w)
    l = compressor.compress(s)
    if len(s) < 1000:
        setlx.print(f'{s} |-> {l}')
    setlx.print(f'size of dictionary: {compressor.mNextCode}')
    numberBits = compressor.mCodeSize
    setlx.print(f'bits needed: {numberBits}')
    setlx.print(f'compression factor: {(1.0 * (len(s) * 7) / numberBits)}')
    expander = lzw(w)
    s2 = expander.uncompress(l)
    if len(s) < 1000:
        setlx.print(f'{l} |-> {s2}')
    assert s == s2, 's == s2'
    setlx.print('decompression correct\n\n')


def demoUncompress(l, w):
    [l, w] = setlx.copy([l, w])
    setlx.print(f'uncompressing {l}')
    expander = lzw(w)
    s = expander.uncompress(l)
    if len(s) < 1000:
        setlx.print(f'{l} |-> {s}')


demoUncompress(setlx.List([98, 97, 98, 128, 129, 130]), True)
demo('babbaabbb', True)


def fileDemo(f):
    [f] = setlx.copy([f])
    setlx.print(f'compressing file {f}')
    s = setlx.sum(setlx.readFile(f))
    demo(s, False)
