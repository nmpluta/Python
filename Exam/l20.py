# -*- coding: utf-8 -*-
# L20 (31) policzy liczbę liczb na liście, które zawierają się z danym przedziale (włącznie z granicami przedziału).

def l20(lst, low, high):
    return sum([low <= e <= high for e in lst])


print(l20([1, -1, 1, 2, 3, 4, 4, 7], 2, 4))
print(l20([1, -1, 1, 2, 3, 4, 4, 7], 2, 3))
