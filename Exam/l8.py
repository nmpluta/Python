# -*- coding: utf-8 -*-
# L8 (11) zwróci True wtedy i tylko wtedy jeżeli dwie podane listy mają przynajmniej jeden wspólny element

def l8(lst1, lst2):
    for e in lst1:
        if e in lst2:
            return True
    return False


lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 1, 8, 9]
lista3 = [10, 11, 12]

print(l8(lista1, lista2))
print(l8(lista1, lista3))
print(l8(lista2, lista3))
