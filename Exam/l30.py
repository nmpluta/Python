# -*- coding: utf-8 -*-
# a) Napisać funkcję, która zamieni wyrazy na liście A na łańcuch "..." jeśli znajdują się na liście B.
#    Fukcja powinna zwracać nową listę.
# b) Zmodyfikować funkcję (a) tak aby liczba kropek odpowiadała liczbei liter w wyrazie.
# c) Zmodyfikować fukcję (a) tak aby nie brała pod uwagę znaku "_" na początku i\albo na końcu wyrazu.
# d) Zmodyfikować fukcję (a) tak aby usuwała wyrazy zamiast ich podmieniania.

def l30a(lstA, lstB):
    return ["..." if strA in lstB else strA for strA in lstA]


def l30b(lstA, lstB):
    return ["." * len(strA) if strA in lstB else strA for strA in lstA]


def l30d(lstA, lstB):
    return list(filter(lambda strA: strA not in lstB, lstA))


listB = ["Test", "12345", "tak"]
listA = ["Testuje", "test", "Test", "funkcji12345", "12345", "jaktak", "tak", "tak dziala"]

print(l30a(listA, listB))
print(l30b(listA, listB))
print(l30d(listA, listB))
