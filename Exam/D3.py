# -*- coding: utf-8 -*-
# D3 (4) sprawdzi czy dany klucz istnieje w danym słowniku.

def d3(dic, key):
    if key in dic.keys():
        return True
    return False


D1 = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d3(D1, 'Olo'))
print(d3(D1, 'Ela'))
print(d3(D1, 'Michał'))
print(d3(D1, 'hjshjhsajhj'))
