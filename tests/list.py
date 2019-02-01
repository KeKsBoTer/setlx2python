from itertools import product

x = []
x = [1,2,3,"test"]
print(x[1-1])
y = x[x[1-1]-1]

a = list(range(1,10))
b = list(range(1,10,3-1))
print(a)
print(b)

a = [x for x in a if x > 2]
a = [c*d for [c,d] in product(a,b) if c > 2]

print(a[10-1:20])