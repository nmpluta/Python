# -*- coding: utf-8 -*-
# D14 stworzy słownik z liczbą pwotórzeń wszystkich liter w łańcuchu bez użycia biblioteki Count

def d14(string):
    char_list = list(string)
    d = {}
    for char in char_list:
        d[char] = d.get(char, 0) + 1
    return d


test = "Ala ma kota"
print(d14(test))
