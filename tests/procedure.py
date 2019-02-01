def p(x, y):
    print(y)
    return x

x = p(1, 2)
print(x)

def procedure_0():
    print("a")

    def procedure_1_0():
        print("a")

    def procedure_1_1():
        print("b")
    [a2, b2] = [procedure_1_0, procedure_1_1]
    a2()
    b2()


def procedure_1():
    print("b")


[a, b] = [procedure_0, procedure_1]
a()
b()
