# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:49:22 2021

@author: HM
"""


def f02_01_secSmallestEl(x):
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
    r = sorted(dict.fromkeys(x))
    if len(r) < 2:
        return None
    return r[1]


# Testing
a = [1, 1, 1.1]
print(f02_01_secSmallestEl(a))

# x.sort()
# l = len(x)
# for i in range(l-1):
#     if x[i+1] != x[i]:
#         return x[i+1]
#     return None