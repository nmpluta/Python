# -*- coding: utf-8 -*-
# L24 (51) podzieli listę co N-ty element (to samo co w L22 tylko z parametrem N).


def l24(lst, N):
    return [lst[i:i + N] for i in range(0, len(lst), N)]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l24(list_1, 2))
print(l24(list_1, 3))
print(l24(list_1, 4))

