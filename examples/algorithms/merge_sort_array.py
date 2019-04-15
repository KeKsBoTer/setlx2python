import setlx


@setlx.procedure
def sort(L: 'rw'):
    A = setlx.copy(L)
    mergeSort(L, 1, len(L) + 1, A)


@setlx.procedure
def mergeSort(L: 'rw', start, end, A: 'rw'):
    if end - start < 2:
        return
    middle = (start + end) // 2
    mergeSort(L, start, middle, A)
    mergeSort(L, middle, end, A)
    merge(L, start, middle, end, A)


@setlx.procedure
def merge(L: 'rw', start, middle, end, A: 'rw'):
    for i in setlx.List(setlx._range(start, end - 1)):
        A[i] = L[i]
    idx1 = setlx.copy(start)
    idx2 = setlx.copy(middle)
    i = setlx.copy(start)
    while idx1 < middle and idx2 < end:
        if A[idx1] <= A[idx2]:
            L[i] = A[idx1]
            idx1 += 1
        else:
            L[i] = A[idx2]
            idx2 += 1
        i += 1
    while idx1 < middle:
        L[i] = A[idx1]
        idx1 += 1
        i += 1
    while idx2 < end:
        L[i] = A[idx2]
        idx2 += 1
        i += 1
    assert idx1 == middle and idx2 == end, 'idx1 == middle && idx2 == end failed'


sort(setlx.List([5, 3, 8, 9, 1, 7, 0, 2, 6, 4]))


@setlx.procedure
def demo():
    L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for n in setlx.List(setlx._range(1, 20))])
    setlx.print(f'L = {L}')
    sort(l)
    setlx.print(f'L = {L}')


@setlx.procedure
def testSort(n, k):
    for i in setlx.List(setlx._range(1, n)):
        L = setlx.List([setlx.rnd(setlx.Set(setlx._range(1, 200))) for x in setlx.List(setlx._range(1, k))])
        C = setlx.copy(L)
        sort(L)
        isOrdered(L)
        sameElements(C, L)
        setlx.print('.')
    setlx.print('All tests successful!')


@setlx.procedure
def isOrdered(L):
    for i in setlx.List(setlx._range(1, len(L) - 1)):
        assert L[i] <= L[i + 1], f'test L[i] <= L[i+1] failed for i = {i}, L = {L}'


@setlx.procedure
def sameElements(L, S):
    assert setlx.collect(L) == setlx.collect(S), 'wrong elements'


demo()
testSort(100, 20)

