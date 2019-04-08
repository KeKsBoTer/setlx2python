import setlx


class tracker:
    ticks = 0


@setlx.procedure
def fibonacci_1(n):
    tracker.ticks += 1
    if n in setlx.List([0, 1]):
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


start = setlx.now()
tracker.ticks = 0
setlx.print(f'Fibonacci Sequence: {setlx.List([fibonacci_1(n) for n in setlx.List(setlx._range(0, 25))])}')
setlx.print(f'({tracker.ticks} ticks)')


@setlx.cached_procedure
def fibonacci_2(n):
    tracker.ticks += 1
    if n in setlx.List([0, 1]):
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


start = setlx.now()
tracker.ticks = 0
setlx.print(f'Fibonacci Sequence: {setlx.List([fibonacci_2(n) for n in setlx.List(setlx._range(0, 25))])}')
setlx.print(f'({tracker.ticks} ticks, {setlx.cacheStats(fibonacci_2)})')

