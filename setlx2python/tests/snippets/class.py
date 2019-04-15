import setlx

class Test:
    # static part
    className = "test"
    setlx.print("static")

    @staticmethod
    @setlx.procedure
    def name(value, self=None):
        if self != None:
            setlx.print("method calls")
        return Test.className

    @setlx.procedure
    def __init__(self, a, b):
        self.name = setlx.to_method(self,Test.name)
        self.mA = mA = setlx.copy(a)
        self.mB = mB = setlx.copy(b)
        setlx.print("constructor")

        @setlx.cached_procedure
        def foo(x):
            return x+self.mA
        self.foo = foo



t = Test(1, 2)
setlx.print(Test.name(20))
setlx.print(t.foo(10))
setlx.print(t.name(20))
