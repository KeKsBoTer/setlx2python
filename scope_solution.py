class Param:
    def __init__(self, value):
        self.value = value

x = 2
def change(x):
	x.value = 3

x_param = Param(x)
change(x_param)
x = x_param.value
print(x)