# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:10:33 2020

@author: User
"""


def listSum3(list):
    sum0 = 0
    sum1 = 0
    sum2 = 0
    for i in range(0, len(list), 3):
        sum0 += list[i]
    for i in range(1, len(list), 3):
        sum1 += list[i]
    for i in range(2, len(list), 3):
        sum2 += list[i]
    return [sum0, sum1, sum2]


# TESTING - OK
# test_list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# test = listSum3(test_list)
# print(test)

"""
Sum of every third element in the list

Parameters
----------
l : list
    List of the numbers (can be empty)

Returns
-------
[sum0, sum1, sum2] : list
    where:
        sum0 = l[0] + l[3] + l[6] ...
        sum1 = l[1] + l[4] + l[7] ...
        sum2 = l[2] + l[5] + l[8] ...

"""
