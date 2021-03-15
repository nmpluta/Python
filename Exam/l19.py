# -*- coding: utf-8 -*-
# L19 (29) usunie z listy powtórzenia

def l19(lst):
    return list(dict.fromkeys(lst))


test = [1, 2, 3, 3, 3, -1, 1, 2]
print(l19(test))
