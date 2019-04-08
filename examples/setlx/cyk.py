import setlx


@setlx.procedure
def cyk(s, rules):
    n = len(s)
    x = setlx.Set()
    for i in setlx.List(setlx._range(1, n)):
        x[[i, i]] = setlx.Set([a for [a, x] in rules if x == s[i]])
    for h in setlx.List(setlx._range(2, n)):
        for i in setlx.List(setlx._range(1, n + 1 - h)):
            x[[i, i + h - 1]] = setlx.Set()
            for k in setlx.List(setlx._range(1, h - 1)):
                x[[i, i + h - 1]] += setlx.Set([a for [a, bc] in rules if bc[1] in x[[i + k - 1]] and bc[2] in x[[i + h - 1]]])
    return x


rules = setlx.Set([setlx.List(['S', 'AB']), setlx.List(['S', 'BC']), setlx.List(['A', 'BA']), setlx.List(['A', 'a']), setlx.List(['B', 'CC']), setlx.List(['B', 'b']), setlx.List(['C', 'AB']), setlx.List(['C', 'a'])])
s = 'ababaa'
n = len(s)
x = cyk(s, rules)
for h in setlx.List(setlx._range(1, n)):
    result = ''
    for i in setlx.List(setlx._range(1, n + 1 - h)):
        result += f'X[{i}, {(i + h - 1)}] = {x[[i + h - 1]]}, '
    setlx.print(result)

