# -*- coding: utf-8 -*-
# D6 (10) zsumuje wszystkie wartości w słowniku.

def d6(dic):
    return sum(map(lambda x: x[1], dic.items()))


d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(d6(d))
