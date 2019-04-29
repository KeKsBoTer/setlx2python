import setlx
from counting_sort import *
extractByte = lambda x, k: x // 256 ** (k - 1) % 256


def radixSort(L):
    [L] = setlx.copy([L])
    for k in setlx.List(setlx._range(1, 4)):
        Grades = setlx.List([(extractByte(x, k) + 1) for x in L])
        L = countingSort(L, Grades)[1]
    return L
