# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:04:37 2021

@author: User
"""

def f02_14_listModNoFor(l):
    """
    Increments the list of integers except for the last element,
    which is decremented.

    Parameters
    ----------
    l : list
        list of integers (can be empty)
    
    Returns
    -------
    list
        list, where all the input elements are incremented and
        the last one is decremented.
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 94
      (docstring and comments are ignored when counting)
    - do not use "import", "for", "while"
    Hint: use map + enumerate
    """
    k = list(map(lambda k: k+1, l))
    if k:
        k[-1] += -2
    return k
    #return list(map(lambda i, k: k+1 if i != (len(l) - 1) else k-1, enumerate(l)))


# Testing
a = [1, 2, 3, 4, 5, 6]
print(f02_14_listModNoFor(a))