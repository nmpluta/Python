# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:36:32 2021

@author: User
"""


def f03_12_alignFloats(l):
    """
    Prints a list floating point numbers aligned to the decimal point.
    Example:

[1.34124, 234.7, 0.32, 1010.12] -> 
   1.34124
 234.7
   0.32
1010.12

    Parameters
    ----------
    l : list
        List of floating point numbers

    Returns
    -------
    None.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 94
      (docstring and comments are ignored when counting)
    - do not use "import",
    """
    for n in l:
        p = len(str(n).split('.')[1])
        print("{:{width}.{precision}f}".format(n, width=1+len(str(max(l)).split('.')[0])+p, precision=p))

    # print('\n\n')
    # print("{:{width}.{precision}f}".format(l[0], width=11, precision=5))
    # print("{:{width}.{precision}f}".format(l[1], width=7, precision=1))
    # print("{:{width}.{precision}f}".format(l[2], width=8, precision=2))
    # print("{:{width}.{precision}f}".format(l[3], width=8, precision=2))
    # print("{:{width}.{precision}f}".format(l[4], width=9, precision=3))


# Testing
f03_12_alignFloats([1.34124, 234.7, 0.32, 1010.12, 12345.789])
