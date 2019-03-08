import setlx

x = []
x = [1, 2, 3, "test"]
setlx.print(x[1-1])
y = x[x[1-1]-1]

a = list(range(1, 10+1))
b = list(range(1, 10+1, 3-1))
setlx.print(a)
setlx.print(b)

a = [x for x in a if x > 2]
a = [c*d for c in a for d in b if c+d > 2]

setlx.print(a[10-1:20])
setlx.print(a[1-1:])
setlx.print(a[:20])
