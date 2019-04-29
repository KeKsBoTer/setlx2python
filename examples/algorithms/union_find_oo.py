import setlx


class unionFind(setlx.SetlXClass):

    @staticmethod
    def union(x, y, self=None):
        [x, y] = setlx.copy([x, y])
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.mHeight[rootX] < self.mHeight[rootY]:
                self.mParent[rootX] = setlx.copy(rootY)
            elif self.mHeight[rootX] > self.mHeight[rootY]:
                self.mParent[rootY] = setlx.copy(rootX)
            else:
                self.mParent[rootY] = setlx.copy(rootX)
                self.mHeight[rootX] += 1

    @staticmethod
    def find(x, self=None):
        [x] = setlx.copy([x])
        p = self.mParent[x]
        if p == x:
            return x
        return self.find(p)

    def __init__(self, M):
        self.find = setlx.to_method(self, unionFind.find, True)
        self.union = setlx.to_method(self, unionFind.union, True)
        [M] = setlx.copy([M])
        self.mParent = setlx.Set([setlx.List([x, x]) for x in M])
        self.mHeight = setlx.Set([setlx.List([x, 1]) for x in M])


def partition(M, R):
    [M, R] = setlx.copy([M, R])
    uf = unionFind(M)
    for [x, y] in R:
        uf.union(x, y)
    Roots = setlx.Set([x for x in M if uf.find(x) == x])
    return setlx.Set([setlx.Set([y for y in M if uf.find(y) == r]) for r in Roots])


def demo():
    M = setlx.Set(setlx._range(1, 9))
    R = setlx.Set([setlx.List([1, 4]), setlx.List([7, 9]), setlx.List([3, 5]), setlx.List([2, 6]), setlx.List([5, 8]), setlx.List([1, 9]), setlx.List([4, 7])])
    setlx.print(f'R = {R}')
    P = partition(M, R)
    setlx.print(f'P = {P}')


demo()
