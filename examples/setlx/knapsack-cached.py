import setlx


@setlx.procedure
def knapsackNaive(problem, maxWeight):
    admissable = setlx.Set([s for s in setlx.pow(problem) if weight(s) <= maxWeight])
    maxValue = setlx.max(setlx.Set([value(s) for s in admissable]))
    return setlx.List([maxValue, setlx.arb(setlx.Set([s for s in admissable if value(s) == maxValue]))])


@setlx.procedure
def weight(s):
    return setlx.sum(setlx.List([w for [_, w, _] in s]))


@setlx.procedure
def value(s):
    return setlx.sum(setlx.List([v for [v, _, _] in s]))


@setlx.cached_procedure
def knapsackDP(problem, maxWeight):
    if problem == setlx.Set():
        return setlx.List([0, setlx.Set()])
    [v, w, k] = setlx.last(problem)
    [v0, s0] = knapsackDP(problem - setlx.Set([setlx.List([v, w, k])]), maxWeight)
    if maxWeight - w >= 0:
        [v1, s1] = knapsackDP(problem - setlx.Set([setlx.List([v, w, k])]), maxWeight - w)
        if v1 + v >= v0:
            return setlx.List([v1 + v, s1 + setlx.Set([setlx.List([v, w, k])])])
    return setlx.List([v0, s0])


@setlx.procedure
def generateProblem(n):
    return setlx.Set([setlx.List([1 + setlx.rnd(20), 1 + setlx.rnd(20), i]) for i in setlx.List(setlx._range(1, n))])


maxWeight = 120
problem = setlx.Set([setlx.List([1, 1, 12]), setlx.List([5, 15, 10]), setlx.List([6, 2, 16]), setlx.List([9, 13, 14]), setlx.List([11, 6, 8]), setlx.List([11, 10, 11]), setlx.List([13, 10, 2]), setlx.List([14, 2, 17]), setlx.List([15, 10, 3]), setlx.List([15, 20, 5]), setlx.List([16, 1, 4]), setlx.List([17, 11, 15]), setlx.List([17, 18, 13]), setlx.List([18, 14, 1]), setlx.List([19, 7, 7]), setlx.List([19, 9, 9]), setlx.List([19, 18, 6])])
start = setlx.now()
[v, s] = knapsackNaive(problem, maxWeight)
stop = setlx.now()
setlx.print('naive algorithm using exhaustive search:')
setlx.print(f's = {s}, value = {v}, weight = {weight(s)}')
start = setlx.now()
[v, s] = knapsackDP(problem, maxWeight)
stop = setlx.now()
setlx.print('greedy algorithm using dynamic programming:')
setlx.print(f's = {s}, value = {v}, weight = {weight(s)}')
setlx.print(setlx.cacheStats(knapsackDP))

