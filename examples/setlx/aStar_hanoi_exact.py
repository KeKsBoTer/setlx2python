import setlx


@setlx.procedure
def aStar(s, t):
    g = predecessor = f = setlx.Set()
    g[s] = 0
    f[s] = h(s)
    openQueue = setlx.Set([setlx.List([f[s], s])])
    while openQueue != setlx.Set():
        [fx, x] = setlx.fromB(openQueue)
        if x in t:
            printPath(s, t, x, fx, predecessor)
            return
        for [y, yCost] in transition(x):
            if g[y] == None or g[x] + yCost < g[y]:
                predecessor[y] = x
                g[y] = g[x] + yCost
                openQueue -= setlx.Set([setlx.List([f[y], y])])
                f[y] = g[y] + h(y)
                openQueue += setlx.Set([setlx.List([f[y], y])])
    setlx.print(f'path {s} -> {t}: no solution')


@setlx.procedure
def h(x):
    n = setlx.max(setlx.sum(x))
    return numberSteps(x, n)


@setlx.procedure
def numberSteps(x, n):
    if n == 0:
        return 0
    n3 = len(x[3])
    if n3 > 0 and setlx.last(x[3]) == n:
        return numberSteps(setlx.List([x[1], x[2], x[3][1:n3 - 1]]), n - 1)
    [last1, last2] = setlx.List([0, 0])
    if len(x[1]) > 0:
        last1 = setlx.last(x[1])
    if len(x[2]) > 0:
        last2 = setlx.last(x[2])
    if last1 >= last2:
        [maxIdx, minIdx] = setlx.List([1, 2])
    else:
        [maxIdx, minIdx] = setlx.List([2, 1])
    [tMax, tMin] = setlx.List([x[maxIdx], x[minIdx]])
    m = len(tMax)
    return numberSteps(setlx.List([tMax[1:m - 1], x[3], tMin]), n - 1) + 2 ** (n - 1)


@setlx.procedure
def transition(x):
    return setlx.Set([moveFromTo(x, v_from, to) for v_from in setlx.Set([1, 2, 3]) for to in setlx.Set([1, 2, 3]) - setlx.Set([v_from])])


@setlx.procedure
def moveFromTo(x, v_from, to):
    origin = x[setlx.v_from]
    if len(origin) > 0:
        head = origin[1]
        goal = x[to]
        other = setlx.arb(setlx.Set([1, 2, 3]) - setlx.Set([setlx.v_from, to]))
        if len(goal) == 0 or head < setlx.first(goal):
            new = setlx.List()
            new[setlx.v_from] = origin[2:]
            new[to] = setlx.List([head]) + goal
            new[other] = x[other]
            return setlx.List([new, 1])


@setlx.procedure
def printPath(start, targets, end, cost, predecessor):
    p = end
    path = setlx.List([end])
    while p != start:
        p = predecessor[p]
        path += setlx.List([p])
    setlx.print(f'path {start} -> {targets}:')
    while len(path) > 0:
        setlx.print(setlx.fromE(path))
    setlx.print(f'cost: {cost}')
    setlx.print(f'nodes expanded: {len(predecessor)}')


@setlx.procedure
def hanoi(n):
    setlx.print(f'computing towers of hanoi with {n} disks:')
    aStar(setlx.List([setlx.List(setlx._range(1, n)), setlx.List(), setlx.List()]), setlx.Set([setlx.List([setlx.List(), setlx.List(), setlx.List(setlx._range(1, n))])]))


hanoi(6)

