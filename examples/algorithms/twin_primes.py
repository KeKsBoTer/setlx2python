import setlx


@setlx.procedure
def main():
    testTwinPrimes = 'twinPrimes := procedure(n) {\r\n                              if (isPrime(n) && isPrime(n + 2)) {\r\n                                  return n;\r\n                              }\r\n                              return twinPrimes(n + 1);\r\n                           };'
    testCounterExample = 'counterExample := procedure(x) {\r\n                               while (true) {\r\n                                   if (stops(testTwinPrimes, x) == 0) {\r\n                                       return false  // only finitely many pairs of primes;\r\n                                   }\r\n                                   x += 1;\r\n                               }\r\n                           };'
    if stops(testCounterExample, 1) == 1:
        setlx.print('There is a biggest pair of primes.')
    else:
        setlx.print('There are infinitely many pairs of primes.')

