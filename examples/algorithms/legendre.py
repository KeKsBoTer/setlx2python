import setlx


@setlx.procedure
def main():
    legendre = lambda n: any(setlx.isPrime(k) for k in setlx.List(setlx._range(n ** 2, (n + 1) ** 2)))
    n = setlx.read('input a natural number: ')
    if not legendre(n):
        while True:
            setlx.print('looping')
    setlx.print(f'legendre was right for n = {n}!')


main()

