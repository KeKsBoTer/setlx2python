from setlx.native import *

x = 1
y = 3
z = x
if x == y or x == z:
    print("if")
elif x != z:
    print("else if")
elif x == z:
    print("else if 2")
else:
    print("else")