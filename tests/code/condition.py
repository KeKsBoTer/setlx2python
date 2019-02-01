x = "test"
y = 2
z = None
same = not(x == y and y == z) or (x != y and y != z) or not(x)

print(bool(x) == bool(y))
print(bool(x) != bool(z))
print(not(x) or y)