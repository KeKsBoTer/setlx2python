n = 50000
inCircle = 0
for x in list(range(1, n + 1)):
    if sqrt(random() ** 2 + random() ** 2) <= 1:
        inCircle += 1
pseudoPi = 4 * inCircle / n
print('pi := $ pseudoPi $ (or $ nDecimalPlaces(pseudoPi, 5) $), which is almost $mathConst(\\"pi\\")$')

