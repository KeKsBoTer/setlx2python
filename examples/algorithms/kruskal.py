﻿import setlx
setlx.load('union-find-oo.stlx')


@setlx.procedure
def mst(V, E):
    uf = unionFind(V)
    Result = setlx.Set()
    for [w, [x, y]] in E:
        rx = uf.find(x)
        ry = uf.find(y)
        if rx != ry:
            Result += setlx.Set([setlx.List([w, setlx.List([x, y])])])
            uf.union(rx, ry)
            if len(Result) == len(V) - 1:
                return Result


@setlx.procedure
def demoFile(fn):
    data = setlx.readFile(fn)
    Edges = setlx.Set()
    Nodes = setlx.Set()
    for line in data:
        [x, y, weight] = setlx.split(line, ' ')
        Edges += setlx.Set([setlx.List([setlx.double(weight), setlx.List([setlx.int(x), setlx.int(y)])])])
        Nodes += setlx.Set([setlx.int(x), setlx.int(y)])
    tree = mst(Nodes, Edges)
    setlx.print(tree)


demoFile('tinyEWG.txt')

