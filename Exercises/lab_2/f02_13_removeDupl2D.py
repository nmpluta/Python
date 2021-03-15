# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:04:37 2021

@author: User
"""


def f02_13_removeDupl2D(l):
    """
    Removes duplicates from a 2-D list

    Parameters
    ----------
    l : list
        2-dimensional list (list of lists)
    
    Returns
    -------
    list
        2-D list with the duplicated elements removed, in the original order
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 66
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    k = []
    for i in l:
        if i not in k:
            k.append(i)
    return k


# Testing
a = [[1, 2], [3, 4], [5, 6], [1, 2], [1, 3]]
b = [1, 2, 3]
print(f02_13_removeDupl2D(a))
