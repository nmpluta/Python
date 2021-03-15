# -*- coding: utf-8 -*-
# L14 (20) usunie z listy elementy o indeksach 0, 4 i 5 (zwróci nową listę).

def l14(lst):
    length = len(lst)
    if length > 5:
        lst.pop(5)
    if length > 4:
        lst.pop(4)
    if length != 0:
        lst.pop(0)
    return lst


# Testing
list_1 = []
list_2 = [0]
list_3 = [0, 1, 2, 3]
list_4 = [0, 1, 2, 3, 4]
list_5 = [0, 1, 2, 3, 4, 5, 22, 24]

print(l14(list_1))
print(l14(list_2))
print(l14(list_3))
print(l14(list_4))
print(l14(list_5))
