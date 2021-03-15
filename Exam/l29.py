# -*- coding: utf-8 -*-
# L29 sprawdzi czy podane listy łąńcuchów są sobie równe czy różne i zwróci odpowiednio True albo False.
# Porównanie nie ma zależeć od wielkości liter.

def l29(lst_1, lst_2):
    _1 = sorted([e1.upper() for e1 in lst_1])           # sorted gdy kolenosc lancuchow nie ma znaczenia
    _2 = sorted([e2.upper() for e2 in lst_2])           #
    if _1 == _2:
        return True
    else:
        return False


list_1 = ['ala', 'ma', 'kota', 'Alicja', 'posiada', 'psa']
list_2 = ['ala', 'kota', 'ma', 'Alicja', 'psa', 'posiada']
list_3 = ['ala', 'ma', 'słonia', 'Alicja', 'posiada', 'żyrafe']

print(l29(list_1, list_1))
print(l29(list_1, list_2))
print(l29(list_1, list_3))
