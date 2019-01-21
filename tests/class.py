class Test:
    def __init__(self, a, b):
        self.mA = a
        self.mB = b
    
    def foo(self,x):
        return x+self.mA

    className = "test"

    @staticmethod
    def name():
        return Test.className
    
t = Test(1,2)
print(t.foo(10))
print(Test.name())