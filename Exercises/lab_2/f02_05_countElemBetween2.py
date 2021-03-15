# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:40:00 2021

@author: User
"""


def f02_05_countElemBetween2(l, a, b):
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
    - target number of non-white characters for the code: 75
      (docstring and comments are ignored when counting)
    - do not use "import"
    - do not use "for" loop
    - do not use "map" function
    """
    return len(list(filter(lambda x: a < x < b, l)))


a = [-3, -2.5, -2.49, -1, 0, 2.5, 2.6, 4, 5]
print(f02_05_countElemBetween2(a, -2.5, 2.5))

# i = 0
# n = 0
# while i < len(l):
#     if a < l[i] < b:
#         n += 1
#     i += 1
