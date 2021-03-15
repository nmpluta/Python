# -*- coding: utf-8 -*-
# D7 (11) pomnoży wszystkie wartości w słowniku.

def d7(dic, n):
    return {key: value*n for (key, value) in dic.items()}


d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(d7(d, 2))
