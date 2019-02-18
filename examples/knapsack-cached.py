import setlx


@setlx.procedure
def knapsackNaive(problem, maxWeight):
    admissable = {s for s in pow(problem) if weight(s) <= maxWeight}
    maxValue = max({value(s) for s in admissable})
    return [maxValue, arb({s for s in admissable if value(s) == maxValue})]


@setlx.procedure
def weight(s):
    return setlx.sum([w for [_, w, _] in s])


@setlx.procedure
def value(s):
    return setlx.sum([v for [v, _, _] in s])


@setlx.cached_procedure
def knapsackDP(problem, maxWeight):
    if problem == set():
        return [0, set()]
    [v, w, k] = last(problem)
    [v0, s0] = knapsackDP(problem - {[v, w, k]}, maxWeight)
    if maxWeight - w >= 0:
        [v1, s1] = knapsackDP(problem - {[v, w, k]}, maxWeight - w)
        if v1 + v >= v0:
            return [v1 + v, s1 + {[v, w, k]}]
    return [v0, s0]


@setlx.procedure
def generateProblem(n):
    return {[1 + rnd(20), 1 + rnd(20), i] for i in list(range(1, n + 1))}


maxWeight = 120
problem = {[1, 1, 12], [5, 15, 10], [6, 2, 16], [9, 13, 14], [11, 6, 8], [11, 10, 11], [13, 10, 2], [14, 2, 17], [15, 10, 3], [15, 20, 5], [16, 1, 4], [17, 11, 15], [17, 18, 13], [18, 14, 1], [19, 7, 7], [19, 9, 9], [19, 18, 6]}
start = now()
[v, s] = knapsackNaive(problem, maxWeight)
stop = now()
print('naive algorithm using exhaustive search:')
print('s = $s$, value = $v$, weight = $weight(s)$')
start = now()
[v, s] = knapsackDP(problem, maxWeight)
stop = now()
print('greedy algorithm using dynamic programming:')
print('s = $s$, value = $v$, weight = $weight(s)$')
print(cacheStats(knapsackDP))

