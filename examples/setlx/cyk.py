from setlx.native import *
import setlx


@setlx.procedure
def cyk(s, rules):
    n = len(s)
    x = set()
    for i in list(range(1, n + 1)):
        x[[i, i]] = {a for [a, x] in rules if x == s[i - 1]}
    for h in list(range(2, n + 1)):
        for i in list(range(1, n + 1 - h + 1)):
            x[[i, i + h - 1]] = set()
            for k in list(range(1, h - 1 + 1)):
                x[[i, i + h - 1]] += {a for [a, bc] in rules if bc[1 - 1] in x[[i + k - 1] - 1] and bc[2 - 1] in x[[i + h - 1] - 1]}
    return x


rules = {['S', 'AB'], ['S', 'BC'], ['A', 'BA'], ['A', 'a'], ['B', 'CC'], ['B', 'b'], ['C', 'AB'], ['C', 'a']}
s = 'ababaa'
n = len(s)
x = cyk(s, rules)
for h in list(range(1, n + 1)):
    result = ''
    for i in list(range(1, n + 1 - h + 1)):
        result += f'X[{i}, {(i + h - 1)}] = {x[[i + h - 1] - 1]}, '
    print(result)

