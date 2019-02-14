import setlx

class Test:
    # static part
    className = "test"
    print("static")

    @setlx.procedure
    @staticmethod
    def name():
        return Test.className

    @setlx.procedure
    def __init__(self, a, b):
        self.mA = a
        self.mB = b
        print("constructor");
    
    @setlx.procedure
    def foo(self,x):
        return x+self.mA

    
t = Test(1,2)
print(Test.name())
print(t.foo(10))