import setlx


class map:
    find = lambda k: mArray[k]

    @staticmethod
    @setlx.procedure
    def insert(k, v):
        self.mArray[k] = v

    @staticmethod
    @setlx.procedure
    def delete(k):
        self.mArray[k] = None

    @staticmethod
    @setlx.procedure
    def f_str():
        return setlx.str(mArray)

    @setlx.procedure
    def __init__(self, n):
        self.mArray = mArray = setlx.List(setlx._range(1, n))


squares = map(10)
for i in setlx.List(setlx._range(1, 10)):
    squares.insert(i, i * i)
for i in setlx.List(setlx._range(1, 10)):
    setlx.print(f'find({i}) = {squares.find(i)}')
for i in setlx.List(setlx._range(1, 10)):
    squares.delete(i)
setlx.print(f'squares = {squares}')

