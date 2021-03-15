# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:49:22 2021

@author: HM
"""


def f02_01_secSmallestEl(x):
    smallest, sec_smallest = x[0], None
    for element in x[1:]:
        if element < smallest:
            sec_smallest = smallest
            smallest = element
    return sec_smallest


# Testing
a = [1, 0]
print(f02_01_secSmallestEl(a))

"""
Finding the second smallest element in the list

Parameters
----------
x : list
     list of numbers (can be empty)

Returns
-------
number
    the second smallest number in x, if exists
None
    if the second smallest number does not exist

Implementation constraints
--------------------------
- target number of non-white characters for the code: 90
  (docstring and comments are ignored when counting)
- do not use import
"""
