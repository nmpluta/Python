# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:10:33 2020

@author: User
"""


def listSumN(l, n):
    sum = [0] * n
    for i in range(n):
        for j in range(i, len(l), n):
            sum[i] += l[j]
    return sum


#TESTING - OK
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# test_sum = []
# test_sum = listSumN(list, 3)
# print(test_sum)



"""
Sum of every N-th element in the list

Parameters
----------
l : list
    List of the numbers (can be empty)
n : int
    Number of sums that should be created for the list.
    n > 0

Returns
-------
[sum0, sum1, ..., sum(N-1)] : list
    where:
        sum0 = l[0] + l[0+N] + l[0+2*N] ...
        sum1 = l[1] + l[1+N] + l[1+2*N] ...
        ...
        sum(N-1) = l[N-1] + l[N-1+N] + l[N-1+2*N] ...

"""