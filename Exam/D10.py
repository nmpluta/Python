# -*- coding: utf-8 -*-
# D10 (14) posortuje słownik według klucza.

def d10(dic):
    return dict(sorted(dic.items()))


D = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d10(D))
