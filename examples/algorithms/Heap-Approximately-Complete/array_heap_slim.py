import setlx


@setlx.procedure
def prioQueue():
    return setlx.List()


@setlx.procedure
def top(h):
    return h[1]


@setlx.procedure
def insert(h: 'rw', p, v):
    h += setlx.List([setlx.List([p, v])])
    upHeap(h, len(h))


@setlx.procedure
def upHeap(h: 'rw', i):
    if i == 1:
        return
    up = parent(i)
    [p1, v1] = h[i]
    [p2, v2] = h[up]
    if p1 < p2:
        exchange(h, i, up)
        upHeap(h, up)


@setlx.procedure
def remove(h: 'rw'):
    v1 = h[1][2]
    v2 = h[len(h)][2]
    h[1] = h[len(h)]
    h[len(h)] = None
    downHeap(h, 1)


@setlx.procedure
def downHeap(h: 'rw', i):
    l = left(i)
    r = right(i)
    if l <= len(h) and r <= len(h):
        [pl, vl] = h[l]
        [pr, vr] = h[r]
        [p, v] = h[i]
        if p <= pl and p <= pr:
            return
        elif p > pl and pl <= pr:
            exchange(h, l, i)
            downHeap(h, l)
        else:
            exchange(h, r, i)
            downHeap(h, r)
    elif l <= len(h):
        [pl, vl] = h[l]
        [p, v] = h[i]
        if pl < p:
            exchange(h, l, i)
            downHeap(h, l)


@setlx.procedure
def exchange(h: 'rw', i, j):
    [h[i], h[j]] = setlx.List([h[j], h[i]])


parent = lambda i: i // 2
left = lambda i: 2 * i
right = lambda i: 2 * i + 1


@setlx.procedure
def toString(h, i, n):
    if i > len(h):
        return ' ' * n + 'Nil'
    [p, v] = h[i]
    return toString(h, left(i), n + 4) + '\\n' + ' ' * n + f'<{v} |-> {p}>\\n' + toString(h, right(i), n + 4)


@setlx.procedure
def demo():
    data = setlx.readFile('data.txt')
    h = prioQueue()
    for line in data:
        [v, n] = setlx.split(line, ':')
        p = setlx.int(removeWS(n))
        setlx.print(f'insert({p}, {v})')
        insert(h, p, v)
        setlx.print(f'{toString(h, 1, 0)}')
    while h != setlx.List():
        setlx.print(f'top(h) = {top(h)}')
        remove(h)
        setlx.print(f'{toString(h, 1, 0)}')


@setlx.procedure
def removeWS(s):
    ws = setlx.Set([' ', '\\t', '\\n', '\\r', '\\v'])
    return setlx.sum(setlx.List([s[i] for i in setlx.List(setlx._range(1, len(s))) if s[i] not in ws]))


demo()

