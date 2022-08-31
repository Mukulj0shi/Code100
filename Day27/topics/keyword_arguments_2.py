#!usr/bin/env python3
"""
Unlimited arguments can be passed to a function using keyword arguments.
1) Format ==> def func(**kwargs). It allows function to take any number of arguments.
2) kwargs is stored in the form of a dictionary.
3) We can use iterate over dictionary to calculate the results.
4) We can also use positional arguments with kwargs.
"""

def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["a"])              # >>> printing value of key "a"
    for key,value in kwargs.items():
        print(key)
        print(value)

add(a = 1, b = 2, c = 3)



def calculation(n, **kwargs):
    print(kwargs)
    addnumber = kwargs["add"]
    multiplynumber = kwargs["multiply"]
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"{n}")

calculation(2, add = 2, multiply = 3)