import setlx


@setlx.procedure
def computeTimes(a, b):
    n = a
    while n <= b:
        setlx.resetRandom()
        time = 0
        for i in setlx.List(setlx._range(1, 1)):
            l = setlx.List([setlx.rnd(2 * n) for i in setlx.List(setlx._range(1, n))])
            start = setlx.now()
            setlx.sort(l)
            stop = setlx.now()
            time += stop - start
        setlx.print(f'n = {n}, t = {(0.001 * time)}, {(time / (n * setlx.log(n)))}')
        n = setlx.ceil(n * 1.2)


computeTimes(10, 500000)

