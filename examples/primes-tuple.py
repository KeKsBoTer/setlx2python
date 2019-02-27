from setlx.native import *
import setlx


@setlx.procedure
def divisors(p):
    return {t for t in set(range(1, p + 1)) if p % t == 0}


n = 100
primes = [p for p in list(range(2, n + 1)) if divisors(p) == {1, p}]
print(primes)

