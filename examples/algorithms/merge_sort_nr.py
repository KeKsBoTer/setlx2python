import setlx


def sort(L: 'rw'):
    A = setlx.copy(L)
    mergeSort(L, A)


def mergeSort(L: 'rw', A: 'rw'):
    n = 1
    while n < len(L):
        k = 0
        while n * (k + 1) + 1 <= len(L):
            merge(L, n * k + 1, n * (k + 1) + 1, setlx.min(setlx.List([n * (k + 2), len(L)])) + 1, A)
            k += 2
        n *= 2


def merge(L: 'rw', start, middle, end, A: 'rw'):
    [start, middle, end] = setlx.copy([start, middle, end])
    for i in setlx.List(setlx._range(start, end - 1)):
        A[i] = L[i]
    idx1 = setlx.copy(start)
    idx2 = setlx.copy(middle)
    i = setlx.copy(start)
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


def demo():
    L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for n in setlx.List(setlx._range(1, 20))])
    setlx.print(f'L = {L}')
    sort(L)
    setlx.print(f'L = {L}')


def testSort(n, k):
    [n, k] = setlx.copy([n, k])
    for i in setlx.List(setlx._range(1, n)):
        L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for x in setlx.List(setlx._range(1, k))])
        C = setlx.copy(L)
        sort(L)
        isOrdered(L)
        sameElements(C, L)
        setlx.print('.')
    setlx.print('All tests passed!')


def isOrdered(L):
    [L] = setlx.copy([L])
    for i in setlx.List(setlx._range(1, len(L) - 1)):
        assert L[i] <= L[i + 1], f'test L[i] <= L[i+1] failed for i = {i}, L = {L}'


def sameElements(L, S):
    [L, S] = setlx.copy([L, S])
    assert setlx.collect(L) == setlx.collect(S), f'different elements in {L} and {S}'


demo()
testSort(100, 20)


def computeTimes(a, b):
    [a, b] = setlx.copy([a, b])
    n = setlx.copy(a)
    while n <= b:
        setlx.resetRandom()
        time = 0
        for i in setlx.List(setlx._range(1, 1)):
            L = setlx.List([setlx.rnd(2 * n) for i in setlx.List(setlx._range(1, n))])
            start = setlx.now()
            sort(L)
            stop = setlx.now()
            time += setlx.stop - start
        setlx.print(f'n = {n}, t = {(0.001 * time)}, {(time / (n * setlx.log(n)))}, {(time / n ** 2.0)}')
        n = setlx.ceil(n * 1.2)


computeTimes(10, 100000)
