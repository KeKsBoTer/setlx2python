import setlx


@setlx.procedure
def mean(xs):
    return setlx.sum(xs) / len(xs)


@setlx.procedure
def variance(xs):
    mu = mean(xs)
    n = len(xs)
    return setlx.sum(setlx.List([((x - mu) ** 2) for x in xs])) / n


@setlx.procedure
def squaredSum(xs):
    xMean = mean(xs)
    return setlx.sum(setlx.List([((x - xMean) ** 2) for x in xs]))


@setlx.procedure
def sumOfProds(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return setlx.sum(setlx.List([((x - xMean) * (y - yMean)) for [x, y] in setlx.cartesian_product(xs, ys)]))


@setlx.procedure
def regressionB(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return sumOfProds(xs, ys) / squaredSum(xs) + 0.0


@setlx.procedure
def regressionA(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return yMean - regressionB(xs, ys) * xMean + 0.0


@setlx.procedure
def correlation(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return sumOfProds(xs, ys) / setlx.sqrt(squaredSum(xs) * squaredSum(ys))


for n in setlx.List([10, 15, 30]):
    setlx.print(f'n = {n}')
    l = setlx.List(setlx._range(1, 10))
    xs = setlx.List([(i ** 2) for i in setlx.List(setlx._range(1, n))])
    ys = setlx.List([(i ** 3) for i in setlx.List(setlx._range(1, n))])
    setlx.print('regression  coefficient beta  = ', regressionB(xs, ys))
    setlx.print('regression  coefficient alpha = ', regressionA(xs, ys))
    setlx.print('correlation coefficient r     = ', correlation(xs, ys))

