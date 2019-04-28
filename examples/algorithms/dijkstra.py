import setlx


@setlx.procedure
def shortestPath(source, Edges):
    Distance = setlx.Set([setlx.List([source, 0])])
    Fringe = setlx.Set([setlx.List([0, source])])
    Visited = setlx.Set()
    while Fringe != setlx.Set():
        [d, u] = setlx.first(Fringe)
        Fringe -= setlx.Set([setlx.List([d, u])])
        for [v, l] in Edges[u]:
            if Distance[v] == None or d + l < Distance[v]:
                Fringe -= setlx.Set([setlx.List([Distance[v], v])])
                Distance[v] = d + l
                Fringe += setlx.Set([setlx.List([d + l, v])])
        Visited += setlx.Set([u])
    return Distance


Edges = setlx.Set([setlx.List(['a', setlx.Set([setlx.List(['b', 2]), setlx.List(['c', 3])])]), setlx.List(['b', setlx.Set([setlx.List(['d', 1])])]), setlx.List(['c', setlx.Set([setlx.List(['e', 3])])]), setlx.List(['d', setlx.Set([setlx.List(['e', 2]), setlx.List(['f', 4])])]), setlx.List(['e', setlx.Set([setlx.List(['f', 1])])]), setlx.List(['f', setlx.Set()])])
M = setlx.Set([x for [x, _] in Edges])
s = 'a'
sp = shortestPath(s, Edges)
for x in M:
    setlx.print(f'distance({s}, {x}) = {sp[x]}')

