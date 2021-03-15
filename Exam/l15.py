# -*- coding: utf-8 -*-
# L15 (21) przekształcić listę znaków w łańcuch znakowy.

def l15(lst):
    string = ""
    for i in range(len(lst)):
        string += lst[i]
    return string


def l15_v2(lst):
    r = "".join(lst)
    return r


list_1 = ['a', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']
print(l15(list_1))
print(l15_v2(list_1))
