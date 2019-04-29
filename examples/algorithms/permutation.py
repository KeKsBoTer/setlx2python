import setlx


def permute(l):
    [l] = setlx.copy([l])
    if len(l) == 1:
        return l
    k = setlx.rnd(setlx.List(setlx._range(1, len(l))))
    return permute(l[:k - 1] + l[k + 1:]) + setlx.List([l[k]])


for i in setlx.List(setlx._range(1, 50)):
    setlx.print(permute(setlx.List(setlx._range(1, 10))))
