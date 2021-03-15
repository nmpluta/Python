# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:26:34 2021

@author: User
"""

def f03_14_genInterlaced(m, n):
    """
    Generates an interlaced array of int chunks.

    Parameters
    ----------
    m : int
        Number of integers in the chunk.
    n : int
        Number of chunks
    
    Returns
    -------
    list
        List of sublist (chunks). Each chunk is a list of m integers,
        with a difference of n. The number of chunks is n.
        The first number in the chunks are consecutive integers starting 
        from 0.
    
    Examples
    --------
    
    2,3 -> [(0, 3), (1, 4), (2, 5)]
    2,4 -> [(0, 4), (1, 5), (2, 6), (3, 7)]
    3,2 -> [(0, 2, 4), (1, 3, 5)]
    4,2 -> [(0, 2, 4, 6), (1, 3, 5, 7)]

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 81
      (docstring and comments are ignored when counting)
    - do not use "import"
    
    """
    return [tuple([i+j for i in range(0, m*n, n)]) for j in range(n)]


print(f03_14_genInterlaced(2, 4))
print(f03_14_genInterlaced(4, 2))
