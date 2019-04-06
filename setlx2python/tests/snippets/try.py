import setlx

try:
    setlx.throw(1)
except setlx.UserException as e:
    err = setlx.unpack_error(e)
    setlx.print('user error', err)
except Exception as e:
    err = setlx.unpack_error(e)
    setlx.print('language error', err)
except Exception as e:
    err = setlx.unpack_error(e)
    setlx.print('error', err)