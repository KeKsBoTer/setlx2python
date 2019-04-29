import setlx


def approximatePi(n):
    [n] = setlx.copy([n])
    k = 0
    i = 0
    while i < n:
        x = 2 * setlx.random() - 1
        y = 2 * setlx.random() - 1
        r2 = x * x + y * y
        if r2 <= 1:
            k += 1
        i += 1
    return 4.0 * k / n


def main():
    n = 10
    i = 7
    while n <= 100000000:
        p = approximatePi(n)
        pi = setlx.mathConst('Pi')
        blanks = ' ' * i
        setlx.print(f'n = {blanks} {n}: p = {blanks} {p}, error = {(p - pi)}')
        n *= 10
        i -= 1


main()
