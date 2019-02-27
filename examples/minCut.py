from setlx.native import *
import setlx


class stoerWagnerMinCut:

    @setlx.procedure
    def __init__(self, edges):
        self.mNodeCount = len(edges)
        self.mEdges = edges
        self.mEquivNodes = [[i] for i in list(range(1, mNodeCount + 1))]

        @setlx.procedure
        def minCut():
            if mNodeCount == 2:
                s = {x for x in mEquivNodes[1 - 1]}
                t = arb({x for x in set(range(2, len(mEdges) + 1)) if not x in s})
                return [countEdges(s, t), s]
            s = {1}
            q = {[1, v] for v in mEdges[1 - 1]}
            qf = {[v, 1] for v in mEdges[1 - 1]}
            for i in list(range(1, mNodeCount - 1 + 1)):
                [cutNumber, v] = last(q)
                equivV = {x for x in mEquivNodes[v - 1]}
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
                return [c, s]
            return [cutNumber, lastS]
        self.minCut = minCut

        @setlx.procedure
        def updateQueue(q: 'rw', qf: 'rw', nodeSet):
            for v in nodeSet:
                dist = qf[v - 1]
                if dist != None:
                    q -= {[dist, v]}
                    qf -= {[v, dist]}
        self.updateQueue = updateQueue

        @setlx.procedure
        def updateDistances(neighbours, s, q: 'rw', qf: 'rw'):
            for x in neighbours:
                dNew = countEdges(s, x)
                dOld = qf[x - 1]
                if dOld != None:
                    q -= {[dOld, x]}
                    qf -= {[x, dOld]}
                q += {[dNew, x]}
                qf += {[x, dNew]}
        self.updateDistances = updateDistances

        @setlx.procedure
        def adjacent(v, s):
            sEquiv = {y for x in s for y in mEquivNodes[x - 1]}
            return setlx.sum({{y for y in mEdges[x - 1] if not y in sEquiv} for x in mEquivNodes[v - 1]})
        self.adjacent = adjacent

        @setlx.procedure
        def countEdges(s, v):
            return setlx.sum([countEdgesSingle(s, e) for e in mEquivNodes[v - 1]])
        self.countEdges = countEdges

        @setlx.procedure
        def countEdgesSingle(s, v):
            neighbours = {y for y in mEdges[v - 1]}
            count = len({x for x in s if x in neighbours})
            return count
        self.countEdgesSingle = countEdgesSingle

        @setlx.procedure
        def merge(x, y):
            s = mEquivNodes[x - 1]
            t = mEquivNodes[y - 1]
            a = s + t
            b = {x for x in a}
            for n in a:
                self.mEdges[n - 1] = [x for x in mEdges[n - 1] if not x in b]
            for n in a:
                self.mEquivNodes[n - 1] = a
            self.mNodeCount -= 1
        self.merge = merge


@setlx.procedure
def readGraph(file):
    lines = readFile(file)
    n = len(lines)
    edges = [set() for _ in list(range(1, n + 1))]
    for i in list(range(1, n + 1)):
        numbers = split(lines[i - 1], ' ')
        edges[i - 1] = [int(x) for x in numbers if int(x) != i]
    return edges


@setlx.procedure
def testSCC(file):
    edges = readGraph(file)
    graph = stoerWagnerMinCut(edges)
    [d, c] = graph.minCut()
    print('value of minimum cut in $file$ is $d$')
    print('minimum cut: $c$')


testSCC('minCut.data')

