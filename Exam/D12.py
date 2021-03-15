# -*- coding: utf-8 -*-
# D12 (17) usunie duplikaty ze słownika.

def d12(dic):
    seen = {}
    for key, value in dic.items():
        if value not in seen.values():
            seen[key] = value
    return seen


d = {1: [1, 2, 3], 2: 3, 3: [1, 2], 4: [1, 2, 3], 5: 3, 6: [2, 1]}
print(d12(d))
