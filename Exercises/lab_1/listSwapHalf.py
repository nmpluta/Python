# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:32:06 2020

@author: User
"""


def listSwapHalf(list):
    length = len(list)
    half_index = len(list) // 2
    if length == 1:
        return list
    elif length % 2 == 1:
        list = list[-half_index - 1:] + list[:half_index]
    else:
        list = list[-half_index:] + list[:half_index]
    return list


# TESTING - OK
# list1 = [1, 2, 3, 4, 5]
# list1 = listSwapHalf(list1)
# print(list1)
#
# list2 = [1, 2, 3, 4, 5, 6]
# list2 = listSwapHalf(list2)
# print(list2)

"""
The functions swaps the first and the second half of the lists

Parameters
----------
l : list
    Any list (can be empty).

Returns
-------
A list where first half of the list elements are moved to the end, e.g.:
[ 1, 2, 3, 4 ] -> [ 3, 4, 1, 2 ]
[ 1, 2, 3, 4, 5] -> [ 3, 4, 5, 1, 2 ]
[ 'a', 'b'] -> [ 'b', 'a']
[ 'a' ] -> [ 'a' ]
[] -> []
"""
