# -*- coding: utf-8 -*-
# D9 (13) zamieni równoliczne listy klucz, wartość na słownik. Użyć pętli i funkcji zip.

def d9(key_lst, value_lst):
    return {key: value for (key, value) in zip(key_lst, value_lst)}


def d9_v2(key_lst, value_lst):
    return dict(zip(key_lst, value_lst))


D1 = [1, 2, 3]
D2 = ['Ala', 'Olo', 'Bolo']
print(d9(D1, D2))
print(d9_v2(D1, D2))

