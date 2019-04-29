import setlx


def product(m, n):
    [m, n] = setlx.copy([m, n])
    if n == 0:
        return 0
    p = product(m, n // 2)
    if n % 2 == 0:
        return p + p
    else:
        return p + p + m


setlx.print(product(18, 37))
