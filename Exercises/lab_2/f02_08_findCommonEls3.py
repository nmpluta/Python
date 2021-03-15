# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:26:00 2021

@author: User
"""


def f02_08_findCommonEls3(a, b):
    """
    Find common elements of two unique lists. Gives reverse sorted output.

    Parameters
    ----------
    a : list
        List of unique integers (can be empty).
    b : list
        List of unique integers (can be empty).

    Returns
    -------
    list
        List of the integers that are common for both input lists,
        sorted in the descending order.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 78
      (docstring and comments are ignored when counting)
    - do not use "import", "for"
    - you can use "set" once
    """
    c = list(set(a).intersection(b))
    c.reverse()
    return c
