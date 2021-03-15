# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:46 2020

@author: Robert Szczygieł
"""


def listFirstLastSwap(list):
    if len(list) > 1:
        first_element = list[0]
        last_element = list[-1]
        list = [last_element] + list[1:-1] + [first_element]
    return list


# TESTING - OK
# list = [1, 2, 3, 4]
# list = listFirstLastSwap(list)
# print(list)
#
# list2 = ['a', 'b', 'c', ' ']
# list2 = listFirstLastSwap(list2)
# print(list2)
#
# list3 = [1]
# list3 = listFirstLastSwap(list3)
# print(list3)


"""
Swaps first and last element on the list

Parameters
----------
l : list
    Any list (can be empty)

Returns
-------
The list with the first and last elements swapped.

 """
