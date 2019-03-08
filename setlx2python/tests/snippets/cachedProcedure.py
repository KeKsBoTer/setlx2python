import setlx

@setlx.cached_procedure
def p(x, y):
    setlx.print("computed")
    return x+y

p(1, 2)
p(1, 2)
