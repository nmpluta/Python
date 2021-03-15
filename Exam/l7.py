# -*- coding: utf-8 -*-
# l7 (10) znajdzie listę słów dłuższych niż N z podanej listy słów.

def l7(lst, N):
    return [e for e in lst if len(e) > N]


lista = ['ala', 'ma', 'kota', 'Alicja', 'posiada', 'psa']
print(l7(lista, 3))
print(l7(lista, 2))
print(l7(lista, 5))
