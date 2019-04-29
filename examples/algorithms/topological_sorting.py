import setlx


def topoSort(T, D):
    [T, D] = setlx.copy([T, D])
    Parents = setlx.Set([setlx.List([t, setlx.Set()]) for t in T])
    Children = setlx.Set([setlx.List([t, setlx.Set()]) for t in T])
    for [s, t] in D:
        Children[s] += setlx.Set([t])
        Parents[t] += setlx.Set([s])
    Orphans = setlx.Set([t for [t, P] in Parents if P == setlx.Set()])
    Sorted = setlx.List()
    while T != setlx.Set():
        assert Orphans != setlx.Set(), 'The graph is cyclic!'
        t = setlx.v_from(Orphans)
        T -= setlx.Set([t])
        Sorted += setlx.List([t])
        for s in Children[t]:
            Parents[s] -= setlx.Set([t])
            if Parents[s] == setlx.Set():
                Orphans += setlx.Set([s])
    return Sorted


def main():
    T = setlx.Set([5, 7, 3, 11, 8, 2, 9, 10])
    D = setlx.Set([setlx.List([5, 11]), setlx.List([7, 11]), setlx.List([7, 8]), setlx.List([3, 8]), setlx.List([3, 10]), setlx.List([11, 2]), setlx.List([11, 9]), setlx.List([11, 10]), setlx.List([8, 9])])
    S = topoSort(T, D)
    setlx.print(S)


main()
