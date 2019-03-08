import setlx

class Test:
    # static part
    className = "test"
    setlx.print("static")

    @staticmethod
    @setlx.procedure
    def name():
        return Test.className

    @setlx.procedure
    def __init__(self, a, b):
        self.mA = mA = a
        self.mB = mB = b
        setlx.print("constructor")

        @setlx.cached_procedure
        def foo(x):
            return x+self.mA
        self.foo = foo


t = Test(1, 2)
setlx.print(Test.name())
setlx.print(t.foo(10))
