# -*- coding: utf-8 -*-
# L13 (19) zwróci w postaci listy różnicę między dwiema podanymi listami.

def l13(lst1, lst2):
    return [e1 - e2 for e1, e2 in zip(lst1, lst2)]


lista1 = [1, 2, 3, 4, 5]
lista2 = [-1, 2, 3, -4, 5]

print(l13(lista1, lista2))
