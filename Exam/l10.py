# -*- coding: utf-8 -*-
# L10 (14) usunie z listy liczby parzyste.

def l10(lst):
    return [e for e in lst if e % 2 != 0]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 100, 101]
print(l10(lista))

