import setlx

def t(a,*list):
    [a,list] = setlx.copy([a,list])
    setlx.print(*list)

t(1,2,3)

def p(x, y: 'rw', z=1, w=2):
    [x,z,w] = setlx.copy([x,z,w])
    x[1] = "can write to x"
    y[1] = "can write to y"
    return w+z


a = setlx.List(["can't write to x"])
b = setlx.List(["can't write to y"])
p(a, b)
setlx.print(a)
setlx.print(b)
