import setlx


class map:
    find = lambda k, self=None: self.mArray[k]

    @staticmethod
    @setlx.procedure
    def insert(k, v, self=None):
        self.mArray[k] = v

    @staticmethod
    @setlx.procedure
    def delete(k, self=None):
        self.mArray[k] = None

    @staticmethod
    @setlx.procedure
    def f_str(self=None):
        return setlx.str(self.mArray)

    @setlx.procedure
    def __init__(self, n):
        self.f_str = setlx.to_method(self, map.f_str)
        self.delete = setlx.to_method(self, map.delete)
        self.insert = setlx.to_method(self, map.insert)
        self.find = setlx.to_method(self, map.find)
        self.mArray = mArray = setlx.List(setlx._range(1, n))


squares = map(10)
for i in setlx.List(setlx._range(1, 10)):
    squares.insert(i, i * i)
for i in setlx.List(setlx._range(1, 10)):
    setlx.print(f'find({i}) = {squares.find(i)}')
for i in setlx.List(setlx._range(1, 10)):
    squares.delete(i)
setlx.print(f'squares = {squares}')

