import setlx


@setlx.procedure
def ord(c):
    return setlx.arb(setlx.Set([n for n in setlx.List(setlx._range(1, 127)) if c == setlx.char(n)]))


@setlx.procedure
def lessThan(s1, s2):
    if s1 == s2:
        return False
    if s1 == '':
        return True
    if s2 == '':
        return False
    c1 = ord(s1[1])
    c2 = ord(s2[1])
    if c1 < c2:
        return True
    if c1 > c2:
        return False
    assert c1 == c2, f'{c1} != {c2}'
    r1 = s1[2:]
    r2 = s2[2:]
    return lessThan(r1, r2)

