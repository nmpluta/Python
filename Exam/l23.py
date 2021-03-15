# -*- coding: utf-8 -*-
# L23 (46) zwróci nieparzyste elementy z listy.

def l23(lst):
    return list(filter(lambda x: x % 2 != 0, lst))


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l23(list_1))
