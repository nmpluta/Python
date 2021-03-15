# -*- coding: utf-8 -*-
# D4 (5) zamieni dany słownik na listę łańcuchów "kulucz:wartość".

def d4(dic):
    r = []
    for (key, value) in dic.items():
        r.append(f"{key}:{value}")
    return r


def d4_v2(dic):
    return [f"{key}:{value}" for (key, value) in dic.items()]


D1 = {'Olo': 23, 'Bolo': 34, 'Ala': 20, 'Ela': 15}
print(d4(D1))
print(d4_v2(D1))
