import setlx


@setlx.procedure
def sort(L: 'rw'):
    A = L
    mergeSort(L, A)


@setlx.procedure
def mergeSort(L: 'rw', A: 'rw'):
    n = 1
    while n < len(L):
        k = 0
        while n * (k + 1) + 1 <= len(L):
            merge(L, n * k + 1, n * (k + 1) + 1, setlx.min(setlx.List([n * (k + 2), len(L)])) + 1, A)
            k += 2
        n *= 2


@setlx.procedure
def merge(L: 'rw', start, middle, end, A: 'rw'):
    for i in setlx.List(setlx._range(start, end - 1)):
        A[i] = L[i]
    idx1 = start
    idx2 = middle
    i = start
    while idx1 < middle and idx2 < end:
        if A[idx1] <= A[idx2]:
            L[i] = A[idx1]
            i += 1
            idx1 += 1
        else:
            L[i] = A[idx2]
            i += 1
            idx2 += 1
    while idx1 < middle:
        L[i] = A[idx1]
        i += 1
        idx1 += 1
    while idx2 < end:
        L[i] = A[idx2]
        i += 1
        idx2 += 1


@setlx.procedure
def demo():
    L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for n in setlx.List(setlx._range(1, 20))])
    setlx.print(f'L = {L}')
    sort(L)
    setlx.print(f'L = {L}')


@setlx.procedure
def testSort(n, k):
    for i in setlx.List(setlx._range(1, n)):
        L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for x in setlx.List(setlx._range(1, k))])
        C = L
        sort(L)
        isOrdered(L)
        sameElements(C, L)
        setlx.print('.')
    setlx.print('All tests passed!')


@setlx.procedure
def isOrdered(L):
    for i in setlx.List(setlx._range(1, len(L) - 1)):
        assert L[i] <= L[i + 1], f'test L[i] <= L[i+1] failed for i = {i}, L = {L}'


@setlx.procedure
def sameElements(L, S):
    assert setlx.collect(L) == setlx.collect(S), f'different elements in {L} and {S}'


demo()
testSort(100, 20)


@setlx.procedure
def computeTimes(a, b):
    n = a
    while n <= b:
        setlx.resetRandom()
        time = 0
        for i in setlx.List(setlx._range(1, 1)):
            L = setlx.List([setlx.rnd(2 * n) for i in setlx.List(setlx._range(1, n))])
            start = setlx.now()
            sort(L)
            stop = setlx.now()
            time += stop - start
        setlx.print(f'n = {n}, t = {(0.001 * time)}, {(time / (n * setlx.log(n)))}, {(time / n ** 2.0)}')
        n = setlx.ceil(n * 1.2)


computeTimes(10, 100000)

