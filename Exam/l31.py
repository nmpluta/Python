# -*- coding: utf-8 -*-
# Jeśli na liście niema odpowiednika wyraz nalezy zamieniać na "?"
# Przykład:
# A=('kot','pies','koń'); B=('pies:dog','kot:cat') -> ('cat','dog','?')

def l31(lstA, lstB):
    dic = dict(strB.split(':') for strB in lstB)
    return [dic.get(strA, '?') for strA in lstA]


A = ('kot', 'pies', 'koń')
B = ('pies:dog', 'kot:cat')

print(l31(A, B))
