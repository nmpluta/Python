# -*- coding: utf-8 -*-
# D2 (3) połączy dwa słowniki.

def d2(dic_1, dic_2):
    dic_1.update(dic_2)
    return dic_1


D1 = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
D2 = {'Marian': 19, "Ada": 22, "Chris": 44}

print(d2(D1, D2))

