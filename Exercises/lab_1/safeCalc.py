# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:04:12 2020

@author: Robert Szczygiel
"""


def safeCalc(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div" and b != 0:
        return a / b
    else:
        return float("NaN")


# Testing - OK
# test = []
# test.append(safeCalc(-3.2, 2.2, "add"))
# test.append(safeCalc(0, -2, "sub"))
# test.append(safeCalc(0.1, 3.198, "mul"))
# test.append(safeCalc(2, 1.25, "div"))
# test.append(safeCalc(3.0, 0, "div"))
# test.append(safeCalc(1.0, 0.5, "sth"))
#
# for i, element in enumerate(test):
#     print("test", "[", i, "]", " = ", element, sep='')


"""
Function to do safe aritmetic operations.
Returns NaN if trying to divide by 0.

Parameters
----------
a : number (float or int)
b : number (float or int)
op : string, operation code

Returns
-------
a + b when op == "add"
a - b when op == "sub"
a * b when op == "mul"
a / b when op == "div"
NaN (float type) in all other cases

"""
