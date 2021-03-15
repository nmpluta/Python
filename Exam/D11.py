# -*- coding: utf-8 -*-
# D11 (15) zwróci klucz maksymalnej wartości ze słownika

def d11(dic):
    temp = tuple(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    return temp[0][0]


D = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d11(D))
