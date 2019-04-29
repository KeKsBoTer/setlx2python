import setlx
a = 1
for k in setlx.List(setlx._range(1, 10)):
    i = k - 1
    setlx.print(f'a{i} = {a}, {(a / 2 ** i)}, {(1 + 1 / 2 * i * (i + 1))}, {(2 ** i * (1 + 1 / 2 * i * (i + 1)))}')
    a = 2 * a + 2 ** k * k
