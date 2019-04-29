import setlx


def stops(f, x):
    [f, x] = setlx.copy([f, x])
    try:
        if f(x) != None:
            return 1
        else:
            return 0
    except Exception as e:
        e = setlx.unpack_error(e)
        return 2


def alan(x):
    [x] = setlx.copy([x])
    result = stops(x, x)
    if result == 1:
        while True:
            setlx.print('... looping ...')
    return result


def f(s):
    [s] = setlx.copy([s])
    return 1


def loop(s):
    [s] = setlx.copy([s])
    x = 1
    while True:
        x = x + 1
    return x


def loop2(s):
    [s] = setlx.copy([s])
    return loop2(s)


setlx.print(stops(f, 'test'))
setlx.print(stops(loop2, 'hugo'))
setlx.print(stops(loop, 'hugo'))
