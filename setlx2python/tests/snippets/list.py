import setlx
x = setlx.List()
x = setlx.List([1, 2, 3, 'test'])
setlx.print(x[1])
y = x[x[1]]
a = setlx.List(setlx._range(1, 10))
b = setlx.List(setlx._range(1, 10, 3 - 1))
setlx.print(a)
setlx.print(b)
a = setlx.List([x for x in a if x > 2])
a = setlx.List([(c * d) for c in a for d in b if c + d > 2])
setlx.print(a[10:20])
setlx.print(a[1:])
setlx.print(a[:20])

