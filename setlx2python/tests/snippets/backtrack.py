import setlx


@setlx.procedure
def test():
    setlx.print('before backtrack')
    raise setlx.BacktrackException()


try:
    test()
except setlx.BacktrackException:
    setlx.print('after backtrack')

