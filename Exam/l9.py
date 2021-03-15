# -*- coding: utf-8 -*-
# L9 (12) usunie z listy elementy o wartościach 0, 4 i 5.

def l9(lst):
    # return list(filter(lambda e: e not in [0, 4, 5], lst))
    return [e for e in lst if e not in [0, 4, 5]]


list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [0, 4, 5]
list3 = [10, 11, 12, 13, 14]

print(l9(list1))
print(l9(list2))
print(l9(list3))
