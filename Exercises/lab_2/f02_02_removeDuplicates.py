# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:49:24 2021

@author: Huber Mucha
"""


def f02_02_removeDuplicates(x):
    """
    Removing duplicates from the input list

    Parameters
    ----------
    x : list
         list of numbers or strings (can be empty)

    Returns
    -------
    list
        list with removed duplicates

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 58
      (docstring and comments are ignored when counting)
    - do not use import
    """
    return list(dict.fromkeys(x))