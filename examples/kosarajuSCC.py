from setlx.native import *
import setlx
import copy

class kosarajuSCC:

    @setlx.procedure
    def __init__(self, nodeCount, edges, reverse):
        self.mNodeCount = mNodeCount = nodeCount
        self.mEdges = mEdges = edges
        self.mReverse = mReverse = reverse
        self.mMarked = mMarked = [False for _ in list(range(1, mNodeCount + 1))]
        self.mSccId = mSccId = [(-1) for _ in list(range(1, mNodeCount + 1))]
        self.mCount = mCount = 0

        @setlx.procedure
        def scc():
            for v in topologicalSort(mReverse):
                if not mMarked[v - 1]:
                    self.mCount += 1
                    dfs(v)
            sccList = [[] for _ in list(range(1, mCount + 1))]
            for v in list(range(1, mNodeCount + 1)):
                sccList[mSccId[v - 1] - 1] += [v]
            return sccList
        self.scc = scc

        @setlx.procedure
        def dfs(v):
            self.mMarked[v - 1] = True
            self.mSccId[v - 1] = mCount
            for w in mEdges[v - 1]:
                if not mMarked[w - 1]:
                    dfs(w)
        self.dfs = dfs

        @setlx.procedure
        def topologicalSort(edges):
            stack = []
            marked = [False for _ in list(range(1, mNodeCount + 1))]
            for v in list(range(1, mNodeCount + 1)):
                if not marked[v - 1]:
                    print(stack)
                    topologicalDFS(v, edges, marked, stack)
                    print(stack)
            return stack
        self.topologicalSort = topologicalSort

        @setlx.procedure
        def topologicalDFS(v, edges, marked: 'rw', stack: 'rw'):
            marked[v - 1] = True
            for w in edges[v - 1]:
                if not marked[w - 1]:
                    topologicalDFS(w, edges, marked, stack)
            stack = [v] + stack
        self.topologicalDFS = topologicalDFS

        @setlx.procedure
        def getCount():
            return mCount
        self.getCount = getCount


@setlx.procedure
def readGraph(file):
    lines = readFile(file)
    [numberNodes, numberEdges] = split(lines[1 - 1], ' ')
    n = int(numberNodes)
    m = int(numberEdges)
    edges = [[] for _ in list(range(1, n + 1))]
    reverse = [[] for _ in list(range(1, n + 1))]
    for i in list(range(1, m + 1)):
        [x, y] = split(lines[i + 1 - 1], ' ')
        nodeX = int(x)
        nodeY = int(y)
        edges[nodeX - 1] += [nodeY]
        reverse[nodeY - 1] += [nodeX]
    return [n, edges, reverse]


@setlx.procedure
def testSCC(file):
    [n, e, r] = readGraph(file)
    sccId = kosarajuSCC(n, e, r)
    sccId.scc()
    print(f'number of strongly connected components in {file} is {sccId.getCount()}')


testSCC('kosarajuSCC.data')

