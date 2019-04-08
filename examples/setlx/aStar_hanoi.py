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
    return setlx.sum(setlx.Set([(2 ** (disk - 1)) for disk in x[1]])) + setlx.sum(setlx.Set([(2 ** (disk - 1)) for disk in x[2]])) * 1 / 3


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

