import setlx

class Test:
    # static part
    className = "test"
    setlx.print("static")

    @staticmethod
    def name(value, self=None):
        [value] = setlx.copy([value])
        if self != None:
            setlx.print("method calls")
        return Test.className

    def __init__(self, a, b):
        self.name = setlx.to_method(self,Test.name,True)
        [a,b] = setlx.copy([a,b])
        self.mA = mA = setlx.copy(a)
        self.mB = mB = setlx.copy(b)
        setlx.print("constructor")

        @setlx.cached_procedure
        def foo(self, x):
            [x] = setlx.copy([x])
            return x+self.mA
        self.foo = setlx.to_method(self,foo)



t = Test(1, 2)
setlx.print(Test.name(20))
setlx.print(t.foo(10))
setlx.print(t.name(20))
