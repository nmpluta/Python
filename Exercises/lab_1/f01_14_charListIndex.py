# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:22:52 2020

@author: HM
"""


def f01_14_charListIndex(l, e):
    r = []
    for i in range(len(l)):
        if l[i] == e:
            r.append(i)
    return r


# TESTING
l1 = ['e','x','a','m','l','e']
test = f01_14_charListIndex(l1, 'e')
print(test)

"""
Creating a list of index where particular 'element' is located in inputList.
E.g.
    ['e','x','a','m','l','e'], 'e'
    returns: [0,5]

Parameters
----------
l : list
    List of chars (can be empty)
e : char

Returns
-------
r : list
    List of indexes.
"""
