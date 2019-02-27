from setlx.native import *
import setlx


@setlx.procedure
def computeEuler(n):
    e = 1
    f = 1
    for i in list(range(1, n + 1)):
        e = e + 1 / f
        f = f * (i + 1)
        print(nDecimalPlaces(e, n))
    return e


print('Computing e to 158 digits')
e = computeEuler(158)
print(nDecimalPlaces(e, 158))

