# -*- coding: utf-8 -*-
# L33 skopresować wyrazy na liście wg. przykłądu.
# PRzykład: in: ('pies','kot','kot','zaba','kon','kon','kon','panda')
# out: (('pies',1),('kot',2),((zaba,1),('kon',3),('panda',1))

def l33(lst):
    seen = {}

    for e in lst:
        if e in list(seen.keys()):
            seen[e] += 1
        else:
            seen[e] = 1
    return tuple(seen.items())


list_1 = ('pies', 'kot', 'kot', 'zaba', 'kon', 'kon', 'kon', 'panda')
print(l33(list_1))
