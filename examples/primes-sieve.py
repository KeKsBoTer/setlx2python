n = 100
primes = set(range(2, n + 1)) - {(p * q) for p in set(range(2, n + 1)) for q in set(range(2, n + 1))}
print(primes)

