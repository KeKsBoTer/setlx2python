import setlx

setlx.Set()
setlx.Set([1, 2, 3])
setlx.Set(setlx._range(1, 3))
setlx.Set(setlx.List([x for x in setlx.List([1, 2]) if x > 0]))