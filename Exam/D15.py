# -*- coding: utf-8 -*-
# D15 na podstawie listy wyrazów zbuduje słownik wyraz:długość_wyrazu

def d15(string_list):
    return {string: len(string) for string in string_list}


lst = ["testing", "first", "word", "length"]
print(d15(lst))
