﻿import setlx
setlx.load('union-find-2-dot.stlx')


@setlx.procedure
def unionFind(M, R):
    Parent = setlx.Set([setlx.List([x, x]) for x in M])
    Height = setlx.Set([setlx.List([x, 1]) for x in M])
    count = 1
    for [x, y] in R:
        graph2Dot(Parent, f'union-find-example-{count}')
        count += 1
        rootX = find(x, Parent)
        rootY = find(y, Parent)
        if rootX != rootY:
            if Height[rootX] < Height[rootY]:
                Parent[rootX] = rootY
            elif Height[rootX] > Height[rootY]:
                Parent[rootY] = rootX
            else:
                Parent[rootY] = rootX
                Height[rootX] += 1
    graph2Dot(Parent, 'union-find-example')
    Roots = setlx.Set([x for x in M if Parent[x] == x])
    return setlx.Set([setlx.Set([y for y in M if find(y, Parent) == root]) for root in Roots])


@setlx.procedure
def find(x, Parent):
    if Parent[x] == x:
        return x
    return find(Parent[x], Parent)


@setlx.procedure
def demo():
    n = 9
    M = setlx.Set(setlx._range(1, n))
    R = setlx.List([setlx.List([k + 1, k]) for k in M if k < n])
    setlx.print(f'R = {R}')
    P = unionFind(M, R)
    setlx.print(f'P = {P}')


demo()

