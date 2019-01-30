from itertools import product

x = "ab_"
y = "xy_"
for a in x:
    if (a != '_'):
        print(a)

for [a,b] in product(x,y):
    print(a,b)

for [a,b] in product(x,y):
    if a != b:
        print(a,b)
