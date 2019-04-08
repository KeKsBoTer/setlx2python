import setlx


@setlx.procedure
def computeEuler(n):
    e = 1
    f = 1
    for i in setlx.List(setlx._range(1, n)):
        e = e + 1 / f
        f = f * (i + 1)
        setlx.print(setlx.nDecimalPlaces(e, n))
    return e


setlx.print('Computing e to 158 digits')
e = computeEuler(158)
setlx.print(setlx.nDecimalPlaces(e, 158))

