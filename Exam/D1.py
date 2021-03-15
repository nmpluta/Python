# -*- coding: utf-8 -*-
# D1 (1) posortuje słownik według wartości.

def d1(dic):
    return sorted(dic.items(), key=lambda x: x[1])


D = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d1(D))
