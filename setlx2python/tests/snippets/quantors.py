import setlx

a = setlx.List([1,2,3])
any(x+y > 0 for x in a for  y in a)
all(x > 0 for x in a)