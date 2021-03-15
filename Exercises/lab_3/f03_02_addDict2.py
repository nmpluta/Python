# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:16:55 2021

@author: User
"""


def f03_02_addDict2(a, b):
    """
    The function adds two dictionaries, summing up the values for the
    repeated keys.

    Parameters
    ----------
    a : dict
        Dictionary with integer values
    b : dict
        Dictionary with integer values

    Returns
    -------
    dict
        The sum of the dictionaries. For repeated keys, the value is the
        sum of the component values.
        The output dictionary is sorted by keys in the ascending order.
        E.g.:
            {'a':1, 'b':2, 'c':3}, {'b':10, 'a':20, 'd':30}
            -> {'a': 21, 'b': 12, 'c': 3, 'd': 30}
        
   Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 102
      (docstring and comments are ignored when counting)
    - do not use "import", "for", "while"
    """
    k = sorted(set(a) | set(b))
    v = map(lambda l: a.get(l, 0) + b.get(l, 0), k)
    return dict(zip(k, v))


# Testing
a = {'a': 1, 'b': 2, 'c': 3}
b = {'b': 10, 'a': 20, 'd': 30}
print(f03_02_addDict2(a, b))