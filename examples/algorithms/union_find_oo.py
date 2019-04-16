import setlx


class unionFind:

    @staticmethod
    @setlx.procedure
    def union(x, y, self=None):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.mHeight[rootX] < self.mHeight[rootY]:
                self.mParent[rootX] = rootY
            elif self.mHeight[rootX] > self.mHeight[rootY]:
                self.mParent[rootY] = rootX
            else:
                self.mParent[rootY] = rootX
                self.mHeight[rootX] += 1

    @staticmethod
    @setlx.procedure
    def find(x, self=None):
        p = self.mParent[x]
        if p == x:
            return x
        return self.find(p)

    @setlx.procedure
    def __init__(self, M):
        self.find = setlx.to_method(self, unionFind.find)
        self.union = setlx.to_method(self, unionFind.union)
        self.mParent = mParent = setlx.Set([setlx.List([x, x]) for x in M])
        self.mHeight = mHeight = setlx.Set([setlx.List([x, 1]) for x in M])


@setlx.procedure
def partition(M, R):
    uf = unionFind(M)
    for [x, y] in R:
        uf.union(x, y)
    Roots = setlx.Set([x for x in M if uf.find(x) == x])
    return setlx.Set([setlx.Set([y for y in M if uf.find(y) == r]) for r in Roots])


@setlx.procedure
def demo():
    M = setlx.Set(setlx._range(1, 9))
    R = setlx.Set([setlx.List([1, 4]), setlx.List([7, 9]), setlx.List([3, 5]), setlx.List([2, 6]), setlx.List([5, 8]), setlx.List([1, 9]), setlx.List([4, 7])])
    setlx.print(f'R = {R}')
    P = partition(M, R)
    setlx.print(f'P = {P}')


demo()

