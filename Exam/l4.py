# -*- coding: utf-8 -*-
# L4 (5) policzy liczbę łańcuchów w liście, dłuższych niż 5, w których pierwszy i ostatni znak są takie same

def l4(lst):
    count = 0
    # test = []
    for e in lst:
        if len(e) > 5 and e[0] == e[-1]:
            count += 1
            # test.append(e)
    # print(test)
    return count


print(l4(["tralalla", "xsdx", "teeeest", "aaaaaa"]))
