# -*- coding: utf-8 -*-
# L17 (23) zamieni listę z jednym poziomem zagnieźdźenia na liste bez zagnieżdżenia (przykład ((1,2),(3,4) -> (1,2,3,4)).


def l17(lst):
    r = []
    for rows in lst:
        for column in rows:
            r.append(column)
    return r


def l17_v2(lst):
    r = []
    for rows in lst:
        r.extend(rows)
    return r


print(l17([[1, 2], [3, 4], [5, 6]]))
print(l17([[1, 2, 3], [4, 5, 6]]))

print(l17_v2([[1, 2], [3, 4], [5, 6]]))
print(l17_v2([[1, 2, 3], [4, 5, 6]]))
