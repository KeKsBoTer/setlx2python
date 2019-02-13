import setlx

class Test:
    def __init__(self,test):
        self.test = test

@setlx.procedure
def p(x, y: 'rw', z=1, w=2):
    y.test = "can write"
    x.test = "can write"


a = Test("a")
b = Test("b")
p(a,b)
print(a.test)
print(b.test)