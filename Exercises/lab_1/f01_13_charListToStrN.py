# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:17:03 2020

@author: RSz
"""


def f01_13_charListToStrN(l, n):
    new = ""
    for elements in l:
        new += elements * n
    return new


# # TESTING
# l1 = ['A', 'n', 'a', 's', 'e']
# test = f01_13_charListToStrN(l1, 3)
# print(test)

"""
Merges list of chars into a string, repeating each character n times.
E.g.:
    ['a', 'b', 'c'], 3 -> "aaabbbccc"

Parameters
----------
l : list
    List of chars (can be empty)
n : int
    Number of character repeatitions. n >= 0

Returns
-------
r : string
"""
