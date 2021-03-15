# -*- coding: utf-8 -*-
# ## L32
#
# a)	Napisać funkcję, która doda do wyrazów na liście A informacje o kategorii, do której należą.
# 	Przykład:
# 	A = ('kilogram','mouse','tree'); animal = ('dog','cat','mouse'); plant = ('tree','grass','flower'); unit = ('meter','kilogram','newton')
# 	-> ('kilogram:unit','mouse:animal','tree:plant')
#
# b)	Zmodyfikować fukcję (a)	aby wyraz mógł należeć do kilu kategorii
#     Przykład: A=('horse','stone','frog'); animal=('dog','horse','frog'); mammal=('horse','dog'); pet=('cat',)
# 	-> A=('horse:animal:mammal','stone','frog:animal')

def l32a(lst):
    animal = ('dog', 'cat', 'mouse')
    plant = ('tree', 'grass', 'flower')
    unit = ('meter', 'kilogram', 'newton')

    dic = {"animal": animal, "plant": plant, "unit": unit}
    r = []

    for e in lst:
        for key, value in dic.items():
            if e in value:
                e += ":" + key
                r.append(e)
    return r


A = ('kilogram', 'mouse', 'tree')
print(l32a(A))


def l32b(lst):
    animal = ('dog', 'horse', 'frog')
    plant = ('tree', 'grass', 'flower')
    unit = ('meter', 'kilogram', 'newton')
    mammal = ('horse', 'dog')
    pet = ('cat')

    dic = {"animal": animal, "plant": plant, "unit": unit, 'mammal': mammal, 'pet': pet}
    r = []

    for index, element in enumerate(lst):
        r.append(element)
        for key, value in dic.items():
            if element in value:
                r[index] += ":" + key
    return r


B = ('horse', 'stone', 'frog')
print(l32b(B))
