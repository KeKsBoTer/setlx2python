import setlx


@setlx.procedure
def aStar(s, t):
    g = predecessor = f = setlx.Set()
    g[s] = 0
    f[s] = graph.h[s]
    openQueue = setlx.Set([setlx.List([f[s], s])])
    while openQueue != setlx.Set():
        [fx, x] = setlx.fromB(openQueue)
        if x in t:
            printPath(s, t, x, fx, predecessor)
            return
        for [y, yCost] in setlx.map(graph.transition[x]):
            if g[y] == None or g[x] + yCost < g[y]:
                predecessor[y] = x
                g[y] = g[x] + yCost
                openQueue -= setlx.Set([setlx.List([f[y], y])])
                f[y] = g[y] + graph.h[y]
                openQueue += setlx.Set([setlx.List([f[y], y])])
    setlx.print(f'path {s} -> {t}: no solution')


class graph:
    h = setlx.Set([setlx.List([1, 22]), setlx.List([2, 94]), setlx.List([3, 98]), setlx.List([4, 34]), setlx.List([5, 88]), setlx.List([6, 4]), setlx.List([7, 8]), setlx.List([8, 5]), setlx.List([9, 1]), setlx.List([10, 0])])
    transition = setlx.Set([setlx.List([1, setlx.List([4, 13])]), setlx.List([1, setlx.List([5, 65])]), setlx.List([1, setlx.List([10, 53])]), setlx.List([2, setlx.List([9, 29])]), setlx.List([3, setlx.List([2, 7])]), setlx.List([3, setlx.List([4, 13])]), setlx.List([3, setlx.List([9, 11])]), setlx.List([4, setlx.List([3, 12])]), setlx.List([5, setlx.List([7, 55])]), setlx.List([5, setlx.List([10, 35])]), setlx.List([6, setlx.List([5, 12])]), setlx.List([7, setlx.List([4, 8])]), setlx.List([7, setlx.List([8, 11])]), setlx.List([8, setlx.List([9, 9])]), setlx.List([8, setlx.List([6, 39])]), setlx.List([10, setlx.List([6, 17])]), setlx.List([10, setlx.List([7, 14])]), setlx.List([10, setlx.List([8, 23])])])


@setlx.procedure
def printPath(start, targets, end, cost, predecessor):
    p = end
    path = setlx.List([end])
    while p != start:
        p = predecessor[p]
        path += setlx.List([p])
    setlx.print(f'path {start} -> {targets}: {path}, cost = {cost}, {len(predecessor)} nodes expanded')


aStar(1, setlx.Set([6]))
aStar(1, setlx.Set([9]))
aStar(1, setlx.Set([6, 9]))
aStar(3, setlx.Set([7]))

