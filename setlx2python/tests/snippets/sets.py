import setlx

setlx.Set()
setlx.Set((1, 2, 3))
setlx.Set(setlx._range(1, 3))
setlx.Set((x for x in [1, 2] if x > 0))