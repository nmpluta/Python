# -*- coding: utf-8 -*-
# L5 (6) posortuje w porządku rosnącym listę duelementowych krotek według ostatniego elementu w krotce

def l5(lst):
    return list(sorted(lst, key=lambda x: x[-1], reverse=False))


def l5_deciding(lst):
    return list(sorted(lst, key=lambda x: x[-1], reverse=True))


test = [("abc", 11), ("cde", 22), ("xxx", -10)]
print(l5(test))
print(l5_deciding(test))
