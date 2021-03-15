# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:40:00 2021

@author: User
"""


def f02_03_countElemBetween(l, a, b):
    """
    Count elements in the list that are within the range (a,b)

    Parameters
    ----------
    l : list
        List of numbers.
    a : number
    b : number

    Returns
    -------
    int
        Number of elements x in the input list such that a < x < b

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 60
      (docstring and comments are ignored when counting)
    - do not use import
    """
    return sum([a < x < b for x in l])


# Testing
a = [-3, -2.5, -2.49, -1, 0, 2.5, 2.6, 4, 5]
print(f02_03_countElemBetween(a, -2.5, 2.5))

# return len([x for x in l if a < x < b])
