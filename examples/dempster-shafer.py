from setlx.native import *
import setlx


@setlx.procedure
def omega():
    return {row[1 - 1] for row in knowledge.data}


@setlx.procedure
def selectEq(i, n):
    return {row[1 - 1] for row in knowledge.data if row[i - 1] == n}


@setlx.procedure
def selectIn(i, n):
    return {row[1 - 1] for row in knowledge.data if row[i - 1] in n}


@setlx.procedure
def unify(l):
    return {[x1, setlx.sum([y2 for [x2, y2] in l if x2 == x1])] for [x1, y1] in l}


@setlx.procedure
def removeConflict(s):
    c = s[set() - 1]
    if c == None:
        return s
    s -= {[set(), c]}
    return {[e[1 - 1], e[2 - 1] / (1 - c)] for e in s}


@setlx.procedure
def accumulate(x, y):
    return removeConflict(unify([[u[1 - 1] * v[1 - 1], u[2 - 1] * v[2 - 1]] for u in x for v in y]))


@setlx.procedure
def accumulateAll(x):
    result = {[omega(), 1]}
    for y in x:
        result = accumulate(result, y)
    return result


@setlx.procedure
def plausibility(s, n):
    return setlx.sum([e[2 - 1] for e in s if n in e[1 - 1] or isSet(n) and n >= e[1 - 1]])


@setlx.procedure
def believe(s, n):
    return setlx.sum([e[2 - 1] for e in s if {n} == e[1 - 1] or n == e[1 - 1]])


@setlx.procedure
def prettyPrint(evidenceSet):
    es = evidenceSet
    print()
    if len(evidenceSet) > 0:
        while len(evidenceSet) > 0:
            mMax = max(range(evidenceSet))
            for e in evidenceSet:
                if e[2 - 1] == mMax:
                    evidence = e
                    evidenceSet -= {e}
                    break
            m = evidence[2 - 1]
            if evidence[1 - 1] == omega():
                print(f'{nbrFormat(m)} == m( Omega )')
            else:
                print(f'{nbrFormat(m)} == m( {evidence[1 - 1]} )')
        print()
        print('Subject | Plausibility | Believe | Disbelieve')
        print('---------------------------------------------')
        for subject in omega():
            pl = plausibility(es, subject)
            b = believe(es, subject)
            print(f'{subject}\\t|    {nbrFormat(pl)}     |  {nbrFormat(b)}  |   {nbrFormat(1 - pl)}')
    else:
        print('Evidence set is empty!')
    print()


@setlx.procedure
def nbrFormat(value):
    roundValue = 1000
    rVal = 1.0 * (round(value * roundValue) / roundValue)
    result = str(rVal)
    n = len(str(roundValue))
    while len(result) <= n + 1:
        result += '0'
    if len(result) > n + 1:
        result = result[1 - 1:n + 1]
    return result


class knowledge:
    data = {['Tobias', 182, 30, 'brown'], ['Ralf', 169, 55, 'black'], ['Sabine', 195, 17, 'brown'], ['Ulrike', 166, 61, 'gray'], ['Erna', 176, 41, 'blond'], ['Frank', 181, 34, 'blond']}


one = {[selectIn(4, {'brown', 'black'}), 0.88], [omega(), 0.12]}
prettyPrint(one)
two = {[selectIn(2, set(range(180, 200 + 1))), 0.45], [selectIn(2, set(range(0, 170 + 1))), 0.45], [omega(), 0.1]}
prettyPrint(two)
three = {[selectIn(3, set(range(40, 100 + 1))), 0.65], [omega(), 0.35]}
prettyPrint(three)
oneTwoThree = accumulateAll({one, two, three})
prettyPrint(oneTwoThree)
print('-------------------------------------------------------------------------------')
knowledge.data = {['Alfons', 'brown', 'm', 37], ['Klaus', 'black', 'm', 55], ['John', 'blond', 'm', 35], ['Ludger', 'red', 'm', 29], ['Eva', 'blond', 'f', 41], ['Helge', 'blond', 'm', 25], ['Martin', 'black', 'm', 31], ['Petra', 'red', 'f', 19], ['Franka', 'brown', 'f', 51]}
one = {[selectIn(4, set(range(25, 30 + 1))), 0.4], [omega(), 0.6]}
prettyPrint(one)
two = {[selectEq(3, 'f'), 0.8], [omega(), 0.2]}
prettyPrint(two)
three = {[selectEq(2, 'black'), 0.8], [omega(), 0.2]}
prettyPrint(three)
oneTwo = accumulate(one, two)
prettyPrint(oneTwo)
oneTwoThree = accumulate(oneTwo, three)
prettyPrint(oneTwoThree)

