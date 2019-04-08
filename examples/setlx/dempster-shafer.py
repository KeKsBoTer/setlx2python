import setlx


@setlx.procedure
def omega():
    return setlx.Set([row[1] for row in knowledge.data])


@setlx.procedure
def selectEq(i, n):
    return setlx.Set([row[1] for row in knowledge.data if row[i] == n])


@setlx.procedure
def selectIn(i, n):
    return setlx.Set([row[1] for row in knowledge.data if row[i] in n])


@setlx.procedure
def unify(l):
    return setlx.Set([setlx.List([x1, setlx.sum(setlx.List([y2 for [x2, y2] in l if x2 == x1]))]) for [x1, y1] in l])


@setlx.procedure
def removeConflict(s):
    c = s[setlx.Set()]
    if c == None:
        return s
    s -= setlx.Set([setlx.List([setlx.Set(), c])])
    return setlx.Set([setlx.List([e[1], e[2] / (1 - c)]) for e in s])


@setlx.procedure
def accumulate(x, y):
    return removeConflict(unify(setlx.List([setlx.List([u[1] * v[1], u[2] * v[2]]) for u in x for v in y])))


@setlx.procedure
def accumulateAll(x):
    result = setlx.Set([setlx.List([omega(), 1])])
    for y in x:
        result = accumulate(result, y)
    return result


@setlx.procedure
def plausibility(s, n):
    return setlx.sum(setlx.List([e[2] for e in s if n in e[1] or setlx.isSet(n) and n >= e[1]]))


@setlx.procedure
def believe(s, n):
    return setlx.sum(setlx.List([e[2] for e in s if setlx.Set([n]) == e[1] or n == e[1]]))


@setlx.procedure
def prettyPrint(evidenceSet):
    es = evidenceSet
    setlx.print()
    if len(evidenceSet) > 0:
        while len(evidenceSet) > 0:
            mMax = setlx.max(setlx.range(evidenceSet))
            for e in evidenceSet:
                if e[2] == mMax:
                    evidence = e
                    evidenceSet -= setlx.Set([e])
                    break
            m = evidence[2]
            if evidence[1] == omega():
                setlx.print(f'{nbrFormat(m)} == m( Omega )')
            else:
                setlx.print(f'{nbrFormat(m)} == m( {evidence[1]} )')
        setlx.print()
        setlx.print('Subject | Plausibility | Believe | Disbelieve')
        setlx.print('---------------------------------------------')
        for subject in omega():
            pl = plausibility(es, subject)
            b = believe(es, subject)
            setlx.print(f'{subject}\\t|    {nbrFormat(pl)}     |  {nbrFormat(b)}  |   {nbrFormat(1 - pl)}')
    else:
        setlx.print('Evidence set is empty!')
    setlx.print()


@setlx.procedure
def nbrFormat(value):
    roundValue = 1000
    rVal = 1.0 * (setlx.round(value * roundValue) / roundValue)
    result = setlx.str(rVal)
    n = len(setlx.str(roundValue))
    while len(result) <= n + 1:
        result += '0'
    if len(result) > n + 1:
        result = result[1:n + 1]
    return result


class knowledge:
    data = setlx.Set([setlx.List(['Tobias', 182, 30, 'brown']), setlx.List(['Ralf', 169, 55, 'black']), setlx.List(['Sabine', 195, 17, 'brown']), setlx.List(['Ulrike', 166, 61, 'gray']), setlx.List(['Erna', 176, 41, 'blond']), setlx.List(['Frank', 181, 34, 'blond'])])


one = setlx.Set([setlx.List([selectIn(4, setlx.Set(['brown', 'black'])), 0.88]), setlx.List([omega(), 0.12])])
prettyPrint(one)
two = setlx.Set([setlx.List([selectIn(2, setlx.Set(setlx._range(180, 200))), 0.45]), setlx.List([selectIn(2, setlx.Set(setlx._range(0, 170))), 0.45]), setlx.List([omega(), 0.1])])
prettyPrint(two)
three = setlx.Set([setlx.List([selectIn(3, setlx.Set(setlx._range(40, 100))), 0.65]), setlx.List([omega(), 0.35])])
prettyPrint(three)
oneTwoThree = accumulateAll(setlx.Set([one, two, three]))
prettyPrint(oneTwoThree)
setlx.print('-------------------------------------------------------------------------------')
knowledge.data = setlx.Set([setlx.List(['Alfons', 'brown', 'm', 37]), setlx.List(['Klaus', 'black', 'm', 55]), setlx.List(['John', 'blond', 'm', 35]), setlx.List(['Ludger', 'red', 'm', 29]), setlx.List(['Eva', 'blond', 'f', 41]), setlx.List(['Helge', 'blond', 'm', 25]), setlx.List(['Martin', 'black', 'm', 31]), setlx.List(['Petra', 'red', 'f', 19]), setlx.List(['Franka', 'brown', 'f', 51])])
one = setlx.Set([setlx.List([selectIn(4, setlx.Set(setlx._range(25, 30))), 0.4]), setlx.List([omega(), 0.6])])
prettyPrint(one)
two = setlx.Set([setlx.List([selectEq(3, 'f'), 0.8]), setlx.List([omega(), 0.2])])
prettyPrint(two)
three = setlx.Set([setlx.List([selectEq(2, 'black'), 0.8]), setlx.List([omega(), 0.2])])
prettyPrint(three)
oneTwo = accumulate(one, two)
prettyPrint(oneTwo)
oneTwoThree = accumulate(oneTwo, three)
prettyPrint(oneTwoThree)

