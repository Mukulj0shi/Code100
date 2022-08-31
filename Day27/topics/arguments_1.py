#!usr/bin/env python3
"""
Making a function that can take unlimited positional arguments.
1) Format ==> def func(*args). It allows function to take any number of arguments.
2) Here args is stored in the form of a tuple.
"""

def add(*args):
    n = 0
    print(type(args))           #>>>args is stored in form of tuple
    print(args)
    for k in args:
        n = k + n
    print(n)

def multiply(*args):
    multiple = 1
    for number in args:
        multiple = multiple * number
    print (multiple)

add (5, 5, 2)
multiply(2, 5)
