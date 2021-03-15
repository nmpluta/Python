# -*- coding: utf-8 -*-
# L22 (44) zwróci grupy trzech kolejnych liczb na liście (odwrotnie niż w L17).

def l22(lst):
    return [lst[i:i + 3] for i in range(0, len(lst), 3)]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l22(list_1))

