from setlx.native import *
import setlx

x = "ab_"
y = "xy_"
for a in x:
    if (a != '_'):
        print(a)

for [a,b] in setlx.cartesian_product(x,y):
    print(a,b)

for [a,b] in setlx.cartesian_product(x,y):
    if a != b:
        print(a,b)
