import setlx


def shortestPath(source, Edges):
    [source, Edges] = setlx.copy([source, Edges])
    Distance = setlx.Set([setlx.List([source, 0])])
    Fringe = setlx.Set([source])
    while Fringe != setlx.Set():
        u = setlx.v_from(Fringe)
        for [v, l] in Edges[u]:
            if Distance[v] == None or Distance[u] + l < Distance[v]:
                Distance[v] = Distance[u] + l
                Fringe += setlx.Set([v])
    return Distance


Edges = setlx.Set([setlx.List(['a', setlx.Set([setlx.List(['b', 2]), setlx.List(['c', 3])])]), setlx.List(['b', setlx.Set([setlx.List(['d', 1])])]), setlx.List(['c', setlx.Set([setlx.List(['e', 3])])]), setlx.List(['d', setlx.Set([setlx.List(['e', 2]), setlx.List(['f', 4])])]), setlx.List(['e', setlx.Set([setlx.List(['f', 1])])]), setlx.List(['f', setlx.Set()])])
M = setlx.Set([x for [x, _] in Edges])
s = 'a'
sp = shortestPath(s, Edges)
for x in M:
    setlx.print(f'distance({s}, {x}) = {sp[x]}')
