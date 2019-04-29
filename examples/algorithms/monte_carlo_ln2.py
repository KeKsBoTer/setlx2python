import setlx


def approximateLn2(n):
    [n] = setlx.copy([n])
    k = 0
    i = 0
    while i < n:
        x = setlx.random() + 1
        y = setlx.random()
        if x * y <= 1:
            k += 1
        i += 1
    return 1.0 * k / n


def main():
    n = 10
    i = 7
    while n < 1000000000000:
        p = approximateLn2(n)
        ln2 = setlx.log(2)
        blanks = ' ' * i
        setlx.print(f'n = {blanks} {n}: p = {blanks} {p}, error = {(p - ln2)}\n        ')
        n *= 10
        i -= 1


ln2 = approximateLn2(9 * 0.7 * 0.3 * 10 ** 6)
setlx.print(f'ln(2) = {ln2}, error = {(ln2 - setlx.log(2))}\n')
main()
