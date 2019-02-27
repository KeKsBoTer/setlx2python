from setlx.native import *
import setlx


@setlx.procedure
def erlangB(a, n):
    p = a ** n / setlx.factorial(n)
    p /= setlx.sum({(a ** i / setlx.factorial(i)) for i in set(range(0, n + 1))})
    return p


@setlx.procedure
def solveA(n, p, step):
    lastA = a = 0
    while True:
        a += step
        b = erlangB(a, n)
        if b <= p:
            lastA = a
        elif b > p * 1.1:
            break
    return lastA


@setlx.procedure
def solveN(a, p):
    n = 0
    while True:
        n += 1
        b = erlangB(a, n)
        if b <= p:
            return n


@setlx.procedure
def erlangC(a, n):
    p = a ** n * n / (setlx.factorial(n) * (n - a))
    p /= setlx.sum({(a ** i / setlx.factorial(i)) for i in set(range(0, n - 1 + 1))}) + p
    return p


print('maximum A (for N = 5,      P <= 5%) is ', solveA(5, 0.05, 0.0001), '.')
print('minimum N (for A = 1.75,   P <= 7%) is ', solveN(1.75, 0.07), '.')
print('Erlang B  (for A = 0.2*48, N = 20 ) is ', erlangB(0.2 * 48, 20), '.')
print('Erlang C  (for A = 0.2*48, N = 20 ) is ', erlangC(0.2 * 48, 20), '.')

