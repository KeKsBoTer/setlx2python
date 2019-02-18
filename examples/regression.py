import setlx


@setlx.procedure
def mean(xs):
    return setlx.sum(xs) / len(xs)


@setlx.procedure
def variance(xs):
    mu = mean(xs)
    n = len(xs)
    return setlx.sum([((x - mu) ** 2) for x in xs]) / n


@setlx.procedure
def squaredSum(xs):
    xMean = mean(xs)
    return setlx.sum([((x - xMean) ** 2) for x in xs])


@setlx.procedure
def sumOfProds(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return setlx.sum([((x - xMean) * (y - yMean)) for [x, y] in setlx.cartesian_product(xs, ys)])


@setlx.procedure
def regressionB(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return sumOfProds(xs, ys) / squaredSum(xs) + 0.0


@setlx.procedure
def regressionA(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return yMean + 0.0


@setlx.procedure
def correlation(xs, ys):
    xMean = mean(xs)
    yMean = mean(ys)
    return sumOfProds(xs, ys) / sqrt(squaredSum(xs) * squaredSum(ys))


for n in [10, 15, 30]:
    print('n = $n$')
    l = list(range(1, 10 + 1))
    xs = [(i ** 2) for i in list(range(1, n + 1))]
    ys = [(i ** 3) for i in list(range(1, n + 1))]
    print('regression  coefficient beta  = ', regressionB(xs, ys))
    print('regression  coefficient alpha = ', regressionA(xs, ys))
    print('correlation coefficient r     = ', correlation(xs, ys))

