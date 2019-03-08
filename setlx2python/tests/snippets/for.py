import setlx

x = "ab_"
y = "xy_"
for a in x:
    if (a != '_'):
        setlx.print(a)

for [a,b] in setlx.cartesian_product(x,y):
    setlx.print(a,b)

for [a,b] in setlx.cartesian_product(x,y):
    if a != b:
        setlx.print(a,b)
