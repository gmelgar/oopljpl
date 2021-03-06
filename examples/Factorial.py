#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

import functools
import math
import operator
import sys
import time

def factorial_1 (n) :
    if n < 2 :
        return 1
    return n * factorial_1(n - 1)

def factorial_2 (n) :
    def f (n, m) :
        if n < 2 :
            return m
        return f(n - 1 , n * m)
    return f(n, 1)

def factorial_3 (n) :
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_4 (n) :
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_5 (n) :
    return functools.reduce(operator.mul, range(1, n + 1), 1)

def test (f, s) :
    print(f.__name__ + " (" + s + ")")
    assert(f(0) ==   1)
    assert(f(1) ==   1)
    assert(f(2) ==   2)
    assert(f(3) ==   6)
    assert(f(4) ==  24)
    assert(f(5) == 120)

    b = time.clock()
    print(f(100))
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("Factorial.py")
print()

print(sys.version)
print()

test(factorial_1,    "recursion")
test(factorial_2,    "tail recursion")
test(factorial_3,    "while")
test(factorial_4,    "for range")
test(factorial_5,    "functools.reduce range")
test(math.factorial, "python")

print("Done.")

"""
Factorial.py

3.3.3 (default, Jan 19 2014, 10:13:09)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

factorial_1 (recursion)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.036 milliseconds

factorial_2 (tail recursion)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.051 milliseconds

factorial_3 (while)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.015 milliseconds

factorial_4 (for range)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.011 milliseconds

factorial_5 (functools.reduce range)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.013 milliseconds

factorial (python)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.019 milliseconds

Done.
"""
