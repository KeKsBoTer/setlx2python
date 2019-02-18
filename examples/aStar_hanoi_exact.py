import setlx


@setlx.procedure
def aStar(s, t):
    g = predecessor = f = set()
    g[s - 1] = 0
    f[s - 1] = h(s)
    openQueue = {[f[s - 1], s]}
    while openQueue != set():
        [fx, x] = fromB(openQueue)
        if x in t:
            printPath(s, t, x, fx, predecessor)
            return
        for [y, yCost] in transition(x):
            if g[y - 1] == None or g[x - 1] + yCost < g[y - 1]:
                predecessor[y - 1] = x
                g[y - 1] = g[x - 1] + yCost
                openQueue -= {[f[y - 1], y]}
                f[y - 1] = g[y - 1] + h(y)
                openQueue += {[f[y - 1], y]}
    print('path $s$ -> $t$: no solution')


@setlx.procedure
def h(x):
    n = max(setlx.sum(x))
    return numberSteps(x, n)


@setlx.procedure
def numberSteps(x, n):
    if n == 0:
        return 0
    n3 = len(x[3 - 1])
    if n3 > 0 and last(x[3 - 1]) == n:
        return numberSteps([x[1 - 1], x[2 - 1], x[3 - 1][1 - 1:n3 - 1]], n - 1)
    [last1, last2] = [0, 0]
    if len(x[1 - 1]) > 0:
        last1 = last(x[1 - 1])
    if len(x[2 - 1]) > 0:
        last2 = last(x[2 - 1])
    if last1 >= last2:
        [maxIdx, minIdx] = [1, 2]
    else:
        [maxIdx, minIdx] = [2, 1]
    [tMax, tMin] = [x[maxIdx - 1], x[minIdx - 1]]
    m = len(tMax)
    return numberSteps([tMax[1 - 1:m - 1], x[3 - 1], tMin], n - 1) + 2 ** (n - 1)


@setlx.procedure
def transition(x):
    return {moveFromTo(x, from, to) for from in {1, 2, 3} for to in {1, 2, 3} - {from}}


@setlx.procedure
def moveFromTo(x, from, to):
    origin = x[from - 1]
    if len(origin) > 0:
        head = origin[1 - 1]
        goal = x[to - 1]
        other = arb({1, 2, 3} - {from, to})
        if len(goal) == 0 or head < first(goal):
            new = []
            new[from - 1] = origin[2 - 1:]
            new[to - 1] = [head] + goal
            new[other - 1] = x[other - 1]
            return [new, 1]


@setlx.procedure
def printPath(start, targets, end, cost, predecessor):
    p = end
    path = [end]
    while p != start:
        p = predecessor[p - 1]
        path += [p]
    print('path $start$ -> $targets$:')
    while len(path) > 0:
        print(fromE(path))
    print('cost: $cost$')
    print('nodes expanded: $#predecessor$')


@setlx.procedure
def hanoi(n):
    print('computing towers of hanoi with $n$ disks:')
    aStar([list(range(1, n + 1)), [], []], {[[], [], list(range(1, n + 1))]})


hanoi(6)

