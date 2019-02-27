from setlx.native import *
import setlx

try:
    throw(1)
except Exception as e:
    err = setlx.unpack_error(e)
    print("error", err)
