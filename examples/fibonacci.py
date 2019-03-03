from setlx.native import *
import setlx


class tracker:
    ticks = 0


@setlx.procedure
def fibonacci_1(n):
    tracker.ticks += 1
    if n in [0, 1]:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


start = now()
tracker.ticks = 0
print(f'Fibonacci Sequence: {[fibonacci_1(n) for n in list(range(0, 25 + 1))]}')
print(f'({tracker.ticks} ticks)')


@setlx.cached_procedure
def fibonacci_2(n):
    tracker.ticks += 1
    if n in [0, 1]:
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


start = now()
tracker.ticks = 0
print(f'Fibonacci Sequence: {[fibonacci_2(n) for n in list(range(0, 25 + 1))]}')
print(f'({tracker.ticks} ticks, {cacheStats(fibonacci_2)})')

