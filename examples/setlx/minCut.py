import setlx


class stoerWagnerMinCut:

    @setlx.procedure
    def __init__(self, edges):
        self.mNodeCount = mNodeCount = len(edges)
        self.mEdges = mEdges = edges
        self.mEquivNodes = mEquivNodes = setlx.List([setlx.List([i]) for i in setlx.List(setlx._range(1, mNodeCount))])

        @setlx.procedure
        def minCut():
            if mNodeCount == 2:
                s = setlx.Set([x for x in mEquivNodes[1]])
                t = setlx.arb(setlx.Set([x for x in setlx.Set(setlx._range(2, len(mEdges))) if not x in s]))
                return setlx.List([countEdges(s, t), s])
            s = setlx.Set([1])
            q = setlx.Set([setlx.List([1, v]) for v in mEdges[1]])
            qf = setlx.Set([setlx.List([v, 1]) for v in mEdges[1]])
            for i in setlx.List(setlx._range(1, mNodeCount - 1)):
                [cutNumber, v] = setlx.last(q)
                equivV = setlx.Set([x for x in mEquivNodes[v]])
                lastS = s
                s += equivV
                updateQueue(q, qf, equivV)
                neighbours = adjacent(v, s)
                updateDistances(neighbours, s, q, qf)
                vPrev = vLast
                vLast = v
            merge(vPrev, vLast)
            [c, s] = minCut()
            if c < cutNumber:
                return setlx.List([c, s])
            return setlx.List([cutNumber, lastS])
        self.minCut = minCut

        @setlx.procedure
        def updateQueue(q: 'rw', qf: 'rw', nodeSet):
            for v in nodeSet:
                dist = qf[v]
                if dist != None:
                    q -= setlx.Set([setlx.List([dist, v])])
                    qf -= setlx.Set([setlx.List([v, dist])])
        self.updateQueue = updateQueue

        @setlx.procedure
        def updateDistances(neighbours, s, q: 'rw', qf: 'rw'):
            for x in neighbours:
                dNew = countEdges(s, x)
                dOld = qf[x]
                if dOld != None:
                    q -= setlx.Set([setlx.List([dOld, x])])
                    qf -= setlx.Set([setlx.List([x, dOld])])
                q += setlx.Set([setlx.List([dNew, x])])
                qf += setlx.Set([setlx.List([x, dNew])])
        self.updateDistances = updateDistances

        @setlx.procedure
        def adjacent(v, s):
            sEquiv = setlx.Set([y for x in s for y in mEquivNodes[x]])
            return setlx.sum(setlx.Set([setlx.Set([y for y in mEdges[x] if not y in sEquiv]) for x in mEquivNodes[v]]))
        self.adjacent = adjacent

        @setlx.procedure
        def countEdges(s, v):
            return setlx.sum(setlx.List([countEdgesSingle(s, e) for e in mEquivNodes[v]]))
        self.countEdges = countEdges

        @setlx.procedure
        def countEdgesSingle(s, v):
            neighbours = setlx.Set([y for y in mEdges[v]])
            count = len(setlx.Set([x for x in s if x in neighbours]))
            return count
        self.countEdgesSingle = countEdgesSingle

        @setlx.procedure
        def merge(x, y):
            s = mEquivNodes[x]
            t = mEquivNodes[y]
            a = s + t
            b = setlx.Set([x for x in a])
            for n in a:
                self.mEdges[n] = setlx.List([x for x in mEdges[n] if not x in b])
            for n in a:
                self.mEquivNodes[n] = a
            self.mNodeCount -= 1
        self.merge = merge


@setlx.procedure
def readGraph(file):
    lines = setlx.readFile(file)
    n = len(lines)
    edges = setlx.List([setlx.Set() for _ in setlx.List(setlx._range(1, n))])
    for i in setlx.List(setlx._range(1, n)):
        numbers = setlx.split(lines[i], ' ')
        edges[i] = setlx.List([setlx.int(x) for x in numbers if setlx.int(x) != i])
    return edges


@setlx.procedure
def testSCC(file):
    edges = readGraph(file)
    graph = stoerWagnerMinCut(edges)
    [d, c] = graph.minCut()
    setlx.print(f'value of minimum cut in {file} is {d}')
    setlx.print(f'minimum cut: {c}')


testSCC('minCut.data')

