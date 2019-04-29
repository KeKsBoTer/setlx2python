import setlx


def power(m, n):
    [m, n] = setlx.copy([m, n])
    r = setlx.copy(m)
    for i in setlx.Set(setlx._range(2, n)):
        r = r * m
    return r


for n in setlx.List(setlx._range(1, 64)):
    setlx.print(power(2, n))
    setlx.print(power(3, n))
