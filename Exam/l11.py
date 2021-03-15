# -*- coding: utf-8 -*-
# l11 (16) wygeneruje listę kwadratów liczb od 1 do zadanej wartości, a następnie zwróci listę
# zawierającą pięć pierwszych oraz pięć ostatnich elementów z wygenerowanej listy.
# Należy uzyć ujemnego indeksowania. Zwrócona lista nie powinna być zagnieżdrzona.


def l11(n):
    l = [e*e for e in range(1, n+1)]
    if len(l) > 10:
        l = l[:5] + l[-5:]
    return l


print(l11(4))
print(l11(7))
print(l11(10))
print(l11(20))
print(l11(30))


