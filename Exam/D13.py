# -*- coding: utf-8 -*-
# D13 (19) połączyć dwa słowniki klucz:liczba tak aby liczby odpowiadające wspólnym kluczom były zsumowane

def d13(dic_1, dic_2):
    return {key: dic_1.get(key, 0) + dic_2.get(key, 0) for key in sorted(set(dic_1) | set(dic_2))}


d_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d_2 = {1: 4, 5: 7, 8: 32}
print(d13(d_1, d_2))
