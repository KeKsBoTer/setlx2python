from copy import deepcopy

def p(x, y):
    x = deepcopy(x)
    y = deepcopy(y)
    print(y)
    return x

x = p(1, 2)
print(x)