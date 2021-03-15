# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:26:00 2021

@author: User
"""


def f02_09_findCommonEls4(a, b):
    """
    Find common elements of two unique lists. Gives reverse sorted output.

    Parameters
    ----------
    a : list
        List of unique integers (can be empty).
    b : list
        List of unique integers (can be empty).

    Returns
    -------
    list
        List of the integers that are common for both input lists,
        sorted in the descending order.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 93
      (docstring and comments are ignored when counting)
    - do not use "import", "set", "sort", "sorted", "reverse"
    - you can use "for" only once
    """
    r = [e for e in a if e in b]
    k = []
    while r:
        k += [max(r)]
        r.remove(max(r))
    return k


x = [1, 2, 3, 7, 4, 2]
y = [3, 4, 2, 5, 7]
print(f02_09_findCommonEls4(x, y))

# r = [e for e in a if e in b]
# k = []
# while r:
#  k += [(r.pop(r.index(max(r))))]

# i = 0
# while i < len(r):
#     j = i + 1
#     while j < len(r):
#         if r[i] < r[j]:
#             r[i], r[j] = r[j], r[i]
#         j += 1
#     i += 1


# i = 0
# N = len(r)
# while i < N:
#     j = i + 1
#     while j < N:
#         if r[i] < r[j]:
#             t = r[i]
#             r[i] = r[j]
#             r[j] = t
#         j = j + 1
#     i = i + 1
