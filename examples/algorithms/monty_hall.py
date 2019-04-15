import setlx


@setlx.procedure
def calculateChances(n):
    successWoody = 0
    successSmart = 0
    for i in setlx.List(setlx._range(1, n)):
        car = setlx.rnd(setlx.Set(setlx._range(1, 3)))
        choice = setlx.rnd(setlx.Set(setlx._range(1, 3)))
        opened = setlx.rnd(setlx.Set(setlx._range(1, 3)) - setlx.Set([choice, car]))
        last = setlx.arb(setlx.Set(setlx._range(1, 3)) - setlx.Set([choice, opened]))
        if car == choice:
            successWoody += 1
        if car == last:
            successSmart += 1
    setlx.print(f'The first  strategy wins {successWoody} cars.')
    setlx.print(f'The second strategy wins {successSmart} cars.')


calculateChances(100000)

