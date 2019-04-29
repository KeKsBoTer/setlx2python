import setlx


def gcd(a, b):
    [a, b] = setlx.copy([a, b])
    while b != 0:
        [a, b] = setlx.List([b, a % b])
    return a


setlx.print(gcd(666, 123456))
