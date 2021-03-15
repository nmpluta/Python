# -*- coding: utf-8 -*-
# L21 (37) znajdzie wspólne elementy z dwóch list.


def l21(lst1, lst2):
    return list(set(lst1) & set(lst2))


print(l21([1, 2, 3, 1], [1, 2, 11, 23]))

