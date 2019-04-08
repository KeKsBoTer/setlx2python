import setlx
n = 50000
inCircle = 0
for x in setlx.List(setlx._range(1, n)):
    if setlx.sqrt(setlx.random() ** 2 + setlx.random() ** 2) <= 1:
        inCircle += 1
pseudoPi = 4 * inCircle / n
setlx.print(f"pi := {pseudoPi} (or {setlx.nDecimalPlaces(pseudoPi, 5)}), which is almost {setlx.mathConst('pi')}")

