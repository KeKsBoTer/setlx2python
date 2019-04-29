import setlx
from union_find_2_dot import *


def unionFind(M, R):
    [M, R] = setlx.copy([M, R])
    Parent = setlx.Set([setlx.List([x, x]) for x in M])
    count = 1
    for [x, y] in R:
        graph2Dot(Parent, f'union-find-example-{count}')
        setlx.print(f'take union of {x} and {y}')
        count += 1
        rootX = find(x, Parent)
        rootY = find(y, Parent)
        if rootX != rootY:
            Parent[rootY] = setlx.copy(rootX)
    graph2Dot(Parent, 'union-find-example')
    Roots = setlx.Set([x for x in M if Parent[x] == x])
    return setlx.Set([setlx.Set([y for y in M if find(y, Parent) == r]) for r in Roots])


def find(x, Parent):
    [x, Parent] = setlx.copy([x, Parent])
    if Parent[x] == x:
        return x
    return find(Parent[x], Parent)


def demo():
    n = 9
    M = setlx.Set(setlx._range(1, n))
    R = setlx.List([setlx.List([k + 1, k]) for k in M if k < n])
    setlx.print(f'R = {R}')
    P = unionFind(M, R)
    setlx.print(f'P = {P}')


demo()
