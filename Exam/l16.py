# -*- coding: utf-8 -*-
# l16 (22) zwróci listę indeksów, pod którymi dany element występuje na liście


def l16(lst, e):
    r = []
    k = 0
    while True:
        try:
            i = lst.index(e, k)
            k = i + 1
            r.append(i)
        except ValueError:
            break
    return r


def l16_v2(lst, e):
    r = []
    for i in range(len(lst)):
        if lst[i] == e:
            r.append(i)
    return r


list_1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 1, 1, 4, 5]

print(l16(list_1, 1))
print(l16(list_1, 2))
print(l16(list_1, 4))

print(l16_v2(list_1, 1))
print(l16_v2(list_1, 2))
print(l16_v2(list_1, 4))
