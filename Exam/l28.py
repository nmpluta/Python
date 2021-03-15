# -*- coding: utf-8 -*-
# L28 (69) usunie duplikaty z listy list.

def l28(lst2d):
    r = []
    for lst in lst2d:
        if lst not in r:
            r.append(lst)
    return r


list_2d = [[-10, -3], [-10, 3], [6, 3], [3, 6], [3, 6]]
print(l28(list_2d))


