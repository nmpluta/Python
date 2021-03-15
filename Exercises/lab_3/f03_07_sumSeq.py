# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:15:45 2021

@author: User
"""

def f03_07_sumSeq(a, n):
    """
    Calculates the sum of consecutive numbers in the list.

    Parameters
    ----------
    a : list
        List of numbers.
    n : int
        Number of elements to be summed.

    Returns
    -------
    list
        List of numbers. Each number is a sum of n consecutive
        input list members, e.g.:
            [1,2,3,4,5], 2  ->  [3,5,7,9]
            [1,2,3,4,5], 3  ->  [6,9,12]
            
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 70
      (docstring and comments are ignored when counting)
    - do not use: "import"
    """
    return [sum(a[i:i+n]) for i in range(len(a)-n+1)]



# Testing
# test = [1,2,3,4,5]
# print(f03_07_sumSeq(test, 2))
# print(f03_07_sumSeq(test, 3))
