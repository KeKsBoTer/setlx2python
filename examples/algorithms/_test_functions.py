﻿import setlx
s1 = 'simple := procedure(x) { return 0; };'
s2 = 'loop := procedure(x) { while (true) { x := x + 1; } };'
s3 = 'hugo := procedure(x) { return ++x; };'
turing = """alan := procedure(x) {
               result := stops(x, x);
               if (result == 1) {
                   while (true) {
                       print(\\"... looping ...\\");
                    }
                }
                return result;
           };"""


@setlx.procedure
def stops(p, a):
    f = 'loop := procedure(x) { while (true) {} };'
    e = equal(f, p, a)
    if e == 2:
        return 2
    else:
        return 1 - e

