import setlx


def t(a,*list):
    setlx.print(*list)

t(1,2,3)

def p(x , y:'rw', z = 1, w = 2):
    x[1-1] = "can write to x"
    y[1-1] = "can write to y"
    return w+z

a = ["can't write to x"]
b = ["can't write to y"]
p(a,b)
setlx.print(a)
setlx.print(b)