# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:36:35 2021

@author: User
"""


def f03_03_string2Dict1(s):
    """
    The function counts the occurrences of the characters in the string
    and returns the dictionary where the key is a character and the value
    is the number of occurrences.

    Parameters
    ----------
    s : str
        Any string (can by empty).

    Returns
    -------
    dict
        The keys of the dictionary are the chars from the string. The
        value is the number of the occurrences of the char in the string.
        The dictionary is sorted by keys in the ascending order, using 
        standard sorted() function.
        
   Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 66
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    return {k: s.count(k) for k in sorted(set(s))}

    # Testing
    # test_string = 'abc Testing this function'
    # print(f03_03_string2Dict1(test_string))

    # k = sorted(set(s))
    # d = {}
    # while(k):
    #     d[k[0]] = s.count(k[0])
    #     k.pop(0)
    # return d

