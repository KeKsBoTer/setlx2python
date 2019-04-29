import setlx


def power(m, n):
    [m, n] = setlx.copy([m, n])
    if n == 0:
        return 1
    p = power(m, n // 2)
    if n % 2 == 0:
        return p * p
    else:
        return p * p * m


for n in setlx.List(setlx._range(1, 64)):
    setlx.print(power(2, n))
    setlx.print(power(3, n))
