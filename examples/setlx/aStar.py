from setlx.native import *
import setlx


@setlx.procedure
def aStar(s, t):
    g = predecessor = f = set()
    g[s - 1] = 0
    f[s - 1] = graph.h[s - 1]
    openQueue = {[f[s - 1], s]}
    while openQueue != set():
        [fx, x] = fromB(openQueue)
        if x in t:
            printPath(s, t, x, fx, predecessor)
            return
        for [y, yCost] in setlx.map(graph.transition[x - 1]):
            if g[y - 1] == None or g[x - 1] + yCost < g[y - 1]:
                predecessor[y - 1] = x
                g[y - 1] = g[x - 1] + yCost
                openQueue -= {[f[y - 1], y]}
                f[y - 1] = g[y - 1] + graph.h[y - 1]
                openQueue += {[f[y - 1], y]}
    print(f'path {s} -> {t}: no solution')


class graph:
    h = {[1, 22], [2, 94], [3, 98], [4, 34], [5, 88], [6, 4], [7, 8], [8, 5], [9, 1], [10, 0]}
    transition = {[1, [4, 13]], [1, [5, 65]], [1, [10, 53]], [2, [9, 29]], [3, [2, 7]], [3, [4, 13]], [3, [9, 11]], [4, [3, 12]], [5, [7, 55]], [5, [10, 35]], [6, [5, 12]], [7, [4, 8]], [7, [8, 11]], [8, [9, 9]], [8, [6, 39]], [10, [6, 17]], [10, [7, 14]], [10, [8, 23]]}


@setlx.procedure
def printPath(start, targets, end, cost, predecessor):
    p = end
    path = [end]
    while p != start:
        p = predecessor[p - 1]
        path += [p]
    print(f'path {start} -> {targets}: {path}, cost = {cost}, {len(predecessor)} nodes expanded')


aStar(1, {6})
aStar(1, {9})
aStar(1, {6, 9})
aStar(3, {7})

