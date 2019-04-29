import setlx


def shortestPath(source, goal, edges):
    [source, goal, edges] = setlx.copy([source, goal, edges])
    dist = setlx.Set([setlx.List([source, 0])])
    fringe = setlx.Set([setlx.List([0, source])])
    backEdge = setlx.Set()
    while fringe != setlx.Set():
        [d, u] = setlx.first(fringe)
        fringe -= setlx.Set([setlx.List([d, u])])
        if u == goal:
            return constructPath(source, goal, backEdge)
        n = setlx.Set([setlx.List([v, l]) for [v, l] in edges[u] if dist[v] == None or d + l < dist[v]])
        for [v, l] in n:
            fringe -= setlx.Set([setlx.List([dist[v], v])])
            dist[v] = d + l
            fringe += setlx.Set([setlx.List([d + l, v])])
            backEdge[v] = setlx.copy(u)


def constructPath(source, goal, backEdge):
    [source, goal, backEdge] = setlx.copy([source, goal, backEdge])
    if source == goal:
        return setlx.List([source])
    n = backEdge[goal]
    return constructPath(source, n, backEdge) + setlx.List([goal])


edges = setlx.Set([setlx.List(['a', setlx.Set([setlx.List(['b', 2]), setlx.List(['c', 3])])]), setlx.List(['b', setlx.Set([setlx.List(['d', 1])])]), setlx.List(['c', setlx.Set([setlx.List(['e', 3])])]), setlx.List(['d', setlx.Set([setlx.List(['e', 2]), setlx.List(['f', 4])])]), setlx.List(['e', setlx.Set([setlx.List(['f', 1])])]), setlx.List(['f', setlx.Set()])])
s = 'a'
g = 'f'
sp = shortestPath(s, g, edges)
setlx.print(f'shortest path from {s} to {g} is {sp}')
