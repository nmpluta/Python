# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:17:03 2020

@author: HM
"""


def f01_12_charListToStr(l):
    new = ""
    for elements in l:
        new += elements
    return new


# # TESTING
# l1 = ['A', 'n', 'a', 's', 'e']
# test = f01_12_charListToStr(l1)
# print(test)

"""
Merges list of chars into a string

Parameters
----------
l : list
    List of chars (can be empty)

Returns
-------
r : string
"""
