# -*- coding: utf-8 -*-
# D17 Dana jest lista osób w formie listy słowników:
dic_list = ({'name': 'Zawisza', 'age': 35, 'height': 150, 'married': True},
            {'name': 'Malińska', 'age': 25, 'height': 170, 'married': True},
            {'name': 'Adamski', 'age': 15, 'height': 160, 'married': False})


# Napisać funkcję, która zwróci : a) nazwisko najstarszej osoby. b) listę nazwisk osób wyższych niż 150 cm


def d17a(dic_lst):
    age_sorted = sorted(dic_lst, key=lambda i: i['age'], reverse=True)
    return age_sorted[0]['name']


def d17b(dic_lst):
    r = []
    for dic in dic_lst:
        if dic['height'] > 150:
            r.append(dic['name'])
    return r


def d17b_v2(dic_lst):
    selected = list(filter(lambda i: i['height'] > 150, dic_lst))
    return list(map(lambda x: x['name'], selected))


print(d17a(dic_list))
print(d17b(dic_list))
print(d17b_v2(dic_list))
