import setlx


@setlx.procedure
def divisors(p):
    return setlx.Set([t for t in setlx.Set(setlx._range(1, p)) if p % t == 0])


n = 100
primes = setlx.List([p for p in setlx.List(setlx._range(2, n)) if divisors(p) == setlx.Set([1, p])])
setlx.print(primes)

