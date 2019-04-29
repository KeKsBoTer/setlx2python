import setlx


@setlx.cached_procedure
def ord(c):
    [c] = setlx.copy([c])
    return setlx.arb(setlx.Set([n for n in setlx.List(setlx._range(1, 127)) if c == setlx.char(n)]))


def lessThan(s1, s2):
    [s1, s2] = setlx.copy([s1, s2])
    if s1 == s2:
        return False
    if s1 == '':
        return True
    if s2 == '':
        return False
    [c1, c2] = setlx.List([ord(s1[1]), ord(s2[1])])
    if c1 < c2:
        return True
    if c1 > c2:
        return False
    return lessThan(s1[2:], s2[2:])
