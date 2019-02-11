from copy import deepcopy


def p(x, y, z=0):
    x = deepcopy(x)
    z = deepcopy(z)
    print(y)
    return x


x = p(1, 2)
print(x)
