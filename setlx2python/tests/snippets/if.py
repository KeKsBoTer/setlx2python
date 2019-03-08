import setlx

x = 1
y = 3
z = x
if x == y or x == z:
    setlx.print("if")
elif x != z:
    setlx.print("else if")
elif x == z:
    setlx.print("else if 2")
else:
    setlx.print("else")