import setlx

try:
    setlx.throw(1)
except Exception as e:
    err = setlx.unpack_error(e)
    print("error", err)
