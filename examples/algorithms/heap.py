import setlx


class Heap:

    @staticmethod
    @setlx.procedure
    def top():
        return setlx.List([mPriority, mValue])

    @staticmethod
    @setlx.procedure
    def insert(priority, value):
        if isEmpty():
            self.mPriority = priority
            self.mValue = value
            self.mLeft = Heap()
            self.mRight = Heap()
            self.mCount = 1
            return
        self.mCount += 1
        if priority < mPriority:
            if mLeft.mCount > mRight.mCount:
                mRight.insert(mPriority, mValue)
            else:
                mLeft.insert(mPriority, mValue)
            self.mPriority = priority
            self.mValue = value
        elif mLeft.mCount > mRight.mCount:
            mRight.insert(priority, value)
        else:
            mLeft.insert(priority, value)

    @staticmethod
    @setlx.procedure
    def remove():
        assert mCount > 0, 'mCount == 0'
        self.mCount -= 1
        if mLeft.isEmpty():
            update(mRight)
            return
        if mRight.isEmpty():
            update(mLeft)
            return
        if mLeft.mPriority < mRight.mPriority:
            self.mPriority = mLeft.mPriority
            self.mValue = mLeft.mValue
            mLeft.remove()
        else:
            self.mPriority = mRight.mPriority
            self.mValue = mRight.mValue
            mRight.remove()

    @staticmethod
    @setlx.procedure
    def update(t):
        self.mPriority = t.mPriority
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
        self.mCount = t.mCount
    isEmpty = lambda : mCount == 0
    f_str = lambda : toString(0)

    @staticmethod
    @setlx.procedure
    def toString(n):
        if isEmpty():
            return ' ' * n + 'Nil'
        else:
            return mLeft.toString(n + 4) + '\\n' + ' ' * n + '<' + mValue + ', ' + mPriority + '>\\n' + mRight.toString(n + 4)

    @setlx.procedure
    def __init__(self):
        self.mPriority = mPriority = None
        self.mValue = mValue = None
        self.mLeft = mLeft = None
        self.mRight = mRight = None
        self.mCount = mCount = 0


@setlx.procedure
def heapSort(A):
    H = Heap()
    for x in A:
        H.insert(x, x)
    graph2Dot(H, 'heap-example')
    S = setlx.List()
    while not H.isEmpty():
        S += setlx.List([H.top()[1]])
        H.remove()
    return S


@setlx.procedure
def demoHeapSort():
    L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 99))) for n in setlx.List(setlx._range(1, 50))])
    S = heapSort(L)
    setlx.print(L)
    setlx.print(S)


@setlx.procedure
def graph2Dot(tree, file):
    Heap.sNodeId = 0
    graph = 'digraph G {\\n'
    graph += '    ordering = out;'
    graph += '    node [shape = record];\\n'
    count = 0
    Children = setlx.Set()
    NodeDict = setlx.Set()
    assignIds(tree, count, NodeDict, Children)
    for k in setlx.List(setlx._range(1, Heap.sNodeId)):
        L = Children[k]
        if L != None and L != setlx.List():
            graph += f'    n{k} -> ' + setlx.join(setlx.List([f'n{c}' for c in L]), ',')
            graph += ';\\n'
    for k in setlx.List(setlx._range(1, Heap.sNodeId)):
        node = NodeDict[k]
        graph += f'    n{k} [label = \\"{node.mPriority}\\"];\\n'
    graph += '}\\n'
    setlx.writeFile(f'{file}.dot', setlx.List([graph]))
    setlx.run(f'dot -Tpdf {file}.dot -o {file}.pdf')
    setlx.run(f'open {file}.pdf')


@setlx.procedure
def assignIds(H: 'rw', count: 'rw', NodeDict: 'rw', Children: 'rw'):
    if H.mCount == 0:
        return
    Heap.sNodeId += 1
    H.mNodeId = Heap.sNodeId
    NodeDict[H.mNodeId] = H
    assignIds(H.mLeft, count, NodeDict, Children)
    assignIds(H.mRight, count, NodeDict, Children)
    L = setlx.List()
    if H.mLeft.mCount > 0:
        L += setlx.List([H.mLeft.mNodeId])
    if H.mRight.mCount > 0:
        L += setlx.List([H.mRight.mNodeId])
    Children[H.mNodeId] = L


demoHeapSort()

