# -*- coding: utf-8 -*-
# L34 Napisać funkcję, która wyróżni boldem (html: x) liczby.
# Założyć, że liczby są oddzielone spacjami od pozostałych wyrazów. Użyć f-stringów.
# Fpormat liczb nie może ulec zmianie. Przykład:
# in: 'Liczba 7 dzielona przez 2 daje liczbę 3.5 a 1 przez 8 daje liczbę 0.128'
# out: 'Liczba 7 dzielona przez 2 daje liczbę 3.5 a 1 przez 8 daje liczbę 0.128'

def l34(string):
    string = string.split()
    r = []
    for e in string:
        if e.isdigit():
            r.append(f"<b>{e}</b>")
        else:
            r.append(e)
    return " ".join(r)

test = 'Liczba 7 dzielona przez 2 daje liczbę 3.5 a 1 przez 8 daje liczbę 0.128'
print(l34(test))

