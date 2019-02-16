import setlx


class Test:
    # static part
    className = "test"
    print("static")

    @staticmethod
    @setlx.procedure
    def name():
        return Test.className

    @setlx.procedure
    def __init__(self, a, b):
        self.mA = a
        self.mB = b
        print("constructor")

        @setlx.cached_procedure
        def foo(x):
            return x+self.mA
        self.foo = foo


t = Test(1, 2)
print(Test.name())
print(t.foo(10))
