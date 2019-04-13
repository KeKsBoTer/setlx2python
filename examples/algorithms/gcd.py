import setlx


@setlx.procedure
def gcd(a, b):
    while b != 0:
        [a, b] = setlx.List([b, a % b])
    return a


setlx.print(gcd(666, 123456))

