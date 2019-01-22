import itertools

x = "ab_"
y = "xy_"
for a in x:
    print(a)

for [a,b] in itertools.product(x,y):
    print(a,b)

for [a,b] in itertools.product(x,y):
    if a != b:
        print(a,b)
