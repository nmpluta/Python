# -*- coding: utf-8 -*-
# L18 (27) znajdzie drugą najmniejszą liczbę na liście

def l18(lst):
    return sorted(list(set(lst)))[1]


list_1 = [-10, -3, 2, -5, 1, 3, 3, 6, 9, -10]
print(l18(list_1))

