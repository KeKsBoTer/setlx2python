import setlx

m = setlx.Matrix([[1, 2, 3], [1, 2, 3]])
y = m + setlx.Matrix([[1, 0, 0], [0, 0, 1]])
setlx.print(2 * y)