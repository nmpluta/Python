# -*- coding: utf-8 -*-
# L27 (64) połączy łańcuchy z dwóch list w jeden łańcuch.

def l27(lst_1, lst_2):
    r = []
    length = min(len(lst_1), len(lst_2))
    for i in range(length):
        r.append(lst_1[i] + lst_2[i])
    return r


list_1 = ["ABC", "kot", "pies"]
list_2 = ["pierwszy", " drugi", "trzeci!"]

print(l27(list_1, list_2))