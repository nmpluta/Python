# -*- coding: utf-8 -*-
# D8 (12) usunie dany klucz z danego` słownika.

def d8(dic, match):
    return {key: value for (key, value) in dic.items() if key != match}


def d8_v2(dic, match):
    return dict(filter(lambda x: x[0] != match, dic.items()))


D1 = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d8(D1, 'Olo'))
print(d8_v2(D1, 'Olo'))
