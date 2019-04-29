import setlx
s1 = 'simple := procedure(x) { return 0; };'
s2 = 'loop := procedure(x) { while (true) { x := x + 1; } };'
s3 = 'hugo := procedure(x) { return ++x; };'
turing = 'alan := procedure(x) {\r\n               result := stops(x, x);\r\n               if (result == 1) {\r\n                   while (true) {\r\n                       print(\\"... looping ...\\");\r\n                    }\r\n                }\r\n                return result;\r\n           };'


def stops(p, a):
    [p, a] = setlx.copy([p, a])
    f = 'loop := procedure(x) { while (true) {} };'
    e = equal(f, p, a)
    if e == 2:
        return 2
    else:
        return 1 - e
