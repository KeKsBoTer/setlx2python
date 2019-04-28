import setlx


@setlx.procedure
def stops(f, x):
    try:
        if f(x) != None:
            return 1
        else:
            return 0
    except Exception as e:
        e = setlx.unpack_error(e)
        return 2


@setlx.procedure
def alan(x):
    result = stops(x, x)
    if result == 1:
        while True:
            setlx.print('... looping ...')
    return result


@setlx.procedure
def f(s):
    return 1


@setlx.procedure
def loop(s):
    x = 1
    while True:
        x = x + 1
    return x


@setlx.procedure
def loop2(s):
    return loop2(s)


setlx.print(stops(f, 'test'))
setlx.print(stops(loop2, 'hugo'))
setlx.print(stops(loop, 'hugo'))

