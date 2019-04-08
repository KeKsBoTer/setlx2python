import setlx


class kosarajuSCC:

    @setlx.procedure
    def __init__(self, nodeCount, edges, reverse):
        self.mNodeCount = mNodeCount = nodeCount
        self.mEdges = mEdges = edges
        self.mReverse = mReverse = reverse
        self.mMarked = mMarked = setlx.List([False for _ in setlx.List(setlx._range(1, mNodeCount))])
        self.mSccId = mSccId = setlx.List([(-1) for _ in setlx.List(setlx._range(1, mNodeCount))])
        self.mCount = mCount = 0

        @setlx.procedure
        def scc():
            for v in topologicalSort(mReverse):
                if not mMarked[v]:
                    self.mCount += 1
                    dfs(v)
            sccList = setlx.List([setlx.List() for _ in setlx.List(setlx._range(1, mCount))])
            for v in setlx.List(setlx._range(1, mNodeCount)):
                sccList[mSccId[v]] += setlx.List([v])
            return sccList
        self.scc = scc

        @setlx.procedure
        def dfs(v):
            self.mMarked[v] = True
            self.mSccId[v] = mCount
            for w in mEdges[v]:
                if not mMarked[w]:
                    dfs(w)
        self.dfs = dfs

        @setlx.procedure
        def topologicalSort(edges):
            stack = setlx.List()
            marked = setlx.List([False for _ in setlx.List(setlx._range(1, mNodeCount))])
            for v in setlx.List(setlx._range(1, mNodeCount)):
                if not marked[v]:
                    topologicalDFS(v, edges, marked, stack)
            return stack
        self.topologicalSort = topologicalSort

        @setlx.procedure
        def topologicalDFS(v, edges, marked: 'rw', stack: 'rw'):
            marked[v] = True
            for w in edges[v]:
                if not marked[w]:
                    topologicalDFS(w, edges, marked, stack)
            stack = setlx.List([v]) + stack
        self.topologicalDFS = topologicalDFS

        @setlx.procedure
        def getCount():
            return mCount
        self.getCount = getCount


@setlx.procedure
def readGraph(file):
    lines = setlx.readFile(file)
    [numberNodes, numberEdges] = setlx.split(lines[1], ' ')
    n = setlx.int(numberNodes)
    m = setlx.int(numberEdges)
    edges = setlx.List([setlx.List() for _ in setlx.List(setlx._range(1, n))])
    reverse = setlx.List([setlx.List() for _ in setlx.List(setlx._range(1, n))])
    for i in setlx.List(setlx._range(1, m)):
        [x, y] = setlx.split(lines[i + 1], ' ')
        nodeX = setlx.int(x)
        nodeY = setlx.int(y)
        edges[nodeX] += setlx.List([nodeY])
        reverse[nodeY] += setlx.List([nodeX])
    return setlx.List([n, edges, reverse])


@setlx.procedure
def testSCC(file):
    [n, e, r] = readGraph(file)
    sccId = kosarajuSCC(n, e, r)
    sccId.scc()
    setlx.print(f'number of strongly connected components in {file} is {sccId.getCount()}')


testSCC('kosarajuSCC.data')

