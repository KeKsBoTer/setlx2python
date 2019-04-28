import setlx
setlx.load('counting-sort.stlx')
extractByte = lambda x, k: x // 256 ** (k - 1) % 256


@setlx.procedure
def radixSort(L):
    for k in setlx.List(setlx._range(1, 4)):
        Grades = setlx.List([(extractByte(x, k) + 1) for x in L])
        L = countingSort(L, Grades)[1]
    return L

