import setlx


class Heap:

    @staticmethod
    @setlx.procedure
    def top(self=None):
        return setlx.List([self.mPriority, self.mValue])

    @staticmethod
    @setlx.procedure
    def insert(priority, value, self=None):
        if isEmpty():
            self.mPriority = priority
            self.mValue = value
            self.mLeft = Heap()
            self.mRight = Heap()
            self.mCount = 1
            return
        self.mCount += 1
        if priority < self.mPriority:
            if self.mLeft.mCount > self.mRight.mCount:
                self.mRight.insert(self.mPriority, self.mValue)
            else:
                self.mLeft.insert(self.mPriority, self.mValue)
            self.mPriority = priority
            self.mValue = value
        elif self.mLeft.mCount > self.mRight.mCount:
            self.mRight.insert(priority, value)
        else:
            self.mLeft.insert(priority, value)

    @staticmethod
    @setlx.procedure
    def remove(self=None):
        assert self.mCount > 0, 'mCount == 0'
        self.mCount -= 1
        if self.mLeft.isEmpty():
            self.update(self.mRight)
            return
        if self.mRight.isEmpty():
            self.update(self.mLeft)
            return
        if self.mLeft.mPriority < self.mRight.mPriority:
            self.mPriority = self.mLeft.mPriority
            self.mValue = self.mLeft.mValue
            self.mLeft.remove()
        else:
            self.mPriority = self.mRight.mPriority
            self.mValue = self.mRight.mValue
            self.mRight.remove()

    @staticmethod
    @setlx.procedure
    def update(t, self=None):
        self.mPriority = t.mPriority
        self.mValue = t.mValue
        self.mLeft = t.mLeft
        self.mRight = t.mRight
        self.mCount = t.mCount
    isEmpty = lambda self=None: self.mCount == 0
    f_str = lambda self=None: self.toString(0)

    @staticmethod
    @setlx.procedure
    def toString(n, self=None):
        if isEmpty():
            return ' ' * n + 'Nil'
        else:
            return self.mLeft.toString(n + 4) + '\\n' + ' ' * n + '<' + self.mValue + ', ' + self.mPriority + '>\\n' + self.mRight.toString(n + 4)

    @setlx.procedure
    def __init__(self):
        self.toString = setlx.to_method(self, Heap.toString)
        self.f_str = setlx.to_method(self, Heap.f_str)
        self.isEmpty = setlx.to_method(self, Heap.isEmpty)
        self.update = setlx.to_method(self, Heap.update)
        self.remove = setlx.to_method(self, Heap.remove)
        self.insert = setlx.to_method(self, Heap.insert)
        self.top = setlx.to_method(self, Heap.top)
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

