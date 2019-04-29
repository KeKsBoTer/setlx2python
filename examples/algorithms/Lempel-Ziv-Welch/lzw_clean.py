import setlx


class lzw(setlx.SetlXClass):

    @staticmethod
    def compress(s, self=None):
        [s] = setlx.copy([s])
        result = setlx.List()
        idx = 1
        while idx <= len(s):
            p = self.longestPrefix(s, idx)
            result += setlx.List([self.mDictionary[s[idx:p]]])
            if p < len(s):
                self.mDictionary[s[idx:p + 1]] = setlx.copy(self.mNextCode)
                self.mNextCode += 1
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
    def uncompress(l, self=None):
        [l] = setlx.copy([l])
        result = ''
        idx = 1
        code = l[idx]
        old = self.mInverse[code]
        while idx < len(l):
            result += old
            idx += 1
            code = l[idx]
            next = self.mInverse[code]
            if next == None:
                next = old + old[1]
            self.mInverse[self.mNextCode] = old + next[1]
            self.mNextCode += 1
            old = setlx.copy(next)
        result += old
        return result

    def __init__(self):
        self.uncompress = setlx.to_method(self, lzw.uncompress, True)
        self.longestPrefix = setlx.to_method(self, lzw.longestPrefix, True)
        self.compress = setlx.to_method(self, lzw.compress, True)
        self.mDictionary = setlx.Set([setlx.List([setlx.char(i), i]) for i in setlx.List(setlx._range(0, 127))])
        self.mInverse = setlx.Set([setlx.List([i, setlx.char(i)]) for i in setlx.List(setlx._range(0, 127))])
        self.mNextCode = 128


def demo(s):
    [s] = setlx.copy([s])
    if len(s) < 1000:
        setlx.print(f'now compressing "{s}"')
    compressor = lzw()
    l = compressor.compress(s)
    if len(s) < 1000:
        setlx.print(f'{s} |-> {l}')
    setlx.print(f'size of dictionary: {compressor.mNextCode}')
    expander = lzw()
    s2 = expander.uncompress(l)
    if len(s) < 1000:
        setlx.print(f'{l} |-> {s2}')
    assert s == s2, 's == s2'
    setlx.print('decompression correct\n\n')


while True:
    s = setlx.read('enter string to encode ("stop" terminates loop): ')
    if s == 'stop':
        break
    demo(s)


def fileDemo(f):
    [f] = setlx.copy([f])
    setlx.print(f'compressing file {f}')
    s = setlx.sum(setlx.readFile(f))
    demo(s)


fileDemo('alice.txt')
fileDemo('lzw.stlx')
