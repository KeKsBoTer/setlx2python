import setlx


@setlx.procedure
def swap(x, y, A: 'rw'):
    [A[x], A[y]] = setlx.List([A[y], A[x]])


@setlx.procedure
def sink(k, A: 'rw', n):
    while 2 * k <= n:
        j = 2 * k
        if j < n and A[j] > A[j + 1]:
            j += 1
        if A[k] <= A[j]:
            return
        swap(k, j, A)
        k = setlx.copy(j)


@setlx.procedure
def heapSort(A: 'rw'):
    n = len(A)
    for k in setlx.List(setlx._range(n // 2, 1, n // 2 - 1 - n // 2)):
        sink(k, A, n)
    while n > 1:
        swap(1, n, A)
        n -= 1
        sink(1, A, n)


@setlx.procedure
def main():
    S = setlx.Set(setlx._range(10, 99))
    A = setlx.List([setlx.rnd(S) for i in setlx.List(setlx._range(1, 20))])
    setlx.print(A)
    heapSort(A)
    setlx.print(A)


main()

