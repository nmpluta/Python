# -*- coding: utf-8 -*-
# L6 (7) usunie duplikaty z listy.

def l6(lst):
    return list(dict.fromkeys(lst))


test = [1, 2, 3, 3, 3, -1, 1, 2]
print(l6(test))

