# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:04:36 2020

@author: HM
"""


def f01_15_listConvert2d1d(l):
    rows = len(l)
    columns = len(l[0])
    r = []
    for i in range(rows):
        for j in range(columns):
            r.append(l[i][j])
    return r


# TESTING
l1 = [[1, 2], [3, 4]]
test = f01_15_listConvert2d1d(l1)
print(test)


"""
Converting 2d list into 1d list
E.g.
    [[1,2],[3,4]] -> [1,2,3,4]

Parameters
----------
l : list
    Two-dimensional list (can be empty)

Returns
-------
r : list
    One-dimensional list
"""
