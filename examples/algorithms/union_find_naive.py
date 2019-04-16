import setlx


@setlx.procedure
def unionFind(M, R):
    P = setlx.Set([setlx.Set([x]) for x in M])
    for [x, y] in R:
        setlx.print(f'[{x}, {y}]')
        Sx = find(x, P)
        Sy = find(y, P)
        if Sx != Sy:
            P -= setlx.Set([Sx, Sy])
            P += setlx.Set([Sx + Sy])
            setlx.print(P)
    return P


@setlx.procedure
def find(x, P):
    return setlx.arb(setlx.Set([S for S in P if x in S]))


@setlx.procedure
def demo():
    M = setlx.Set(setlx._range(1, 9))
    R = setlx.Set([setlx.List([1, 4]), setlx.List([7, 9]), setlx.List([3, 5]), setlx.List([2, 6]), setlx.List([5, 8]), setlx.List([1, 9]), setlx.List([4, 7])])
    setlx.print(f'R = {R}')
    P = unionFind(M, R)
    setlx.print(f'P = {P}')


demo()

