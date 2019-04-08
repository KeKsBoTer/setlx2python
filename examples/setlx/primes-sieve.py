import setlx
n = 100
primes = setlx.Set(setlx._range(2, n)) - setlx.Set([(p * q) for p in setlx.Set(setlx._range(2, n)) for q in setlx.Set(setlx._range(2, n))])
setlx.print(primes)

