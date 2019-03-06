x = "x"
def p():
    print("p")

t = p

def test(x=1):

    print(vars())
    print(x)
    p()

test()

eval()