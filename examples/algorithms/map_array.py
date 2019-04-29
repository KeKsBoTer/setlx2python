import setlx


class map(setlx.SetlXClass):
    find = lambda k, self=None: self.mArray[k]

    @staticmethod
    def insert(k, v, self=None):
        [k, v] = setlx.copy([k, v])
        self.mArray[k] = setlx.copy(v)

    @staticmethod
    def delete(k, self=None):
        [k] = setlx.copy([k])
        self.mArray[k] = None

    @staticmethod
    def f_str(self=None):
        return setlx.str(self.mArray)

    def __init__(self, n):
        self.f_str = setlx.to_method(self, map.f_str, True)
        self.delete = setlx.to_method(self, map.delete, True)
        self.insert = setlx.to_method(self, map.insert, True)
        self.find = setlx.to_method(self, map.find, True)
        [n] = setlx.copy([n])
        self.mArray = setlx.List(setlx._range(1, n))


squares = map(10)
for i in setlx.List(setlx._range(1, 10)):
    squares.insert(i, i * i)
for i in setlx.List(setlx._range(1, 10)):
    setlx.print(f'find({i}) = {squares.find(i)}')
for i in setlx.List(setlx._range(1, 10)):
    squares.delete(i)
setlx.print(f'squares = {squares}')
