import setlx


class lzw:

    @staticmethod
    @setlx.procedure
    def compress(s, self=None):
        result = setlx.List()
        idx = 1
        while idx <= len(s):
            p = self.longestPrefix(s, idx)
            result += setlx.List([self.mDictionary[s[idx:p]]])
            if p < len(s):
                mDictionary[s[idx:p + 1]] = self.mNextCode
                self.mNextCode += 1
            idx = p + 1
        return result

    @staticmethod
    @setlx.procedure
    def longestPrefix(s, i, self=None):
        oldK = setlx.copy(i)
        k = i + 1
        while k <= len(s) and self.mDictionary[s[i:k]] != None:
            oldK = setlx.copy(k)
            k += 1
        return oldK

    @staticmethod
    @setlx.procedure
    def uncompress(l, self=None):
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
            mInverse[self.mNextCode] = old + next[1]
            self.mNextCode += 1
            old = setlx.copy(next)
        result += old
        return result

    @setlx.procedure
    def __init__(self):
        self.uncompress = setlx.to_method(self, lzw.uncompress)
        self.longestPrefix = setlx.to_method(self, lzw.longestPrefix)
        self.compress = setlx.to_method(self, lzw.compress)
        self.mDictionary = mDictionary = setlx.Set([setlx.List([setlx.char(i), i]) for i in setlx.List(setlx._range(0, 127))])
        self.mInverse = mInverse = setlx.Set([setlx.List([i, setlx.char(i)]) for i in setlx.List(setlx._range(0, 127))])
        self.mNextCode = mNextCode = 128


@setlx.procedure
def demo(s):
    if len(s) < 1000:
        setlx.print(f'now compressing \\"{s}\\')
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
    setlx.print('decompression correct\\n\\n')


while True:
    s = setlx.read('enter string to encode (\\"stop\\" terminates loop): ')
    if s == 'stop':
        break
    demo(s)


@setlx.procedure
def fileDemo(f):
    setlx.print(f'compressing file {f}')
    s = setlx.sum(setlx.readFile(f))
    demo(s)


fileDemo('alice.txt')
fileDemo('lzw.stlx')

