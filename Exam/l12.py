# -*- coding: utf-8 -*-
# L12 (18) wygeneruje wszystkie permutacje bez powtórzeń danej listy.
# Należy zwrócić listę dwuelementowych krotek.

def l12(lst):
    r = []
    for e1 in lst:
        for e2 in lst:
            t = (e1, e2)
            r.append(t)
    return r


print(l12([1, 2]))
print(l12([1, 2, 3]))
print(l12([1, 2, 3, 4]))

