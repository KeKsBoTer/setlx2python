import setlx


@setlx.procedure
def approximatePi(n):
    k = 0
    i = 0
    while i < n:
        x = setlx.random()
        y = 0.5 * (1 + setlx.random())
        if (1 + x * x) * y <= 1:
            k += 1
        i += 1
    return 2 * (k / n + 1.0)


@setlx.procedure
def main():
    n = 10
    i = 7
    while n < 1000000000000:
        p = approximatePi(n)
        pi = setlx.mathConst('Pi')
        blanks = ' ' * i
        setlx.print(f'n = {blanks} {n}: p = {blanks} {p}, error = {(p - pi)}\\n')
        n *= 10
        i -= 1


pia = approximatePi(9 * 0.7 * 0.3 * 10 ** 6)
pi = setlx.mathConst('Pi')
setlx.print(f'pi = {pia}, error = {(pia - pi)}\\n')
main()

