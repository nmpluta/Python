# -*- coding: utf-8 -*-
# L1 (1) zsumuje wszystkie elementy na danej liście.

def sum_elements(list_to_sum):
    list_sum = 0
    for element in list_to_sum:
        list_sum += element
    return list_sum


def sum_el_2(lst):
    return sum(lst)


# TESTING - OK
test_list = [1, 2, 3, 4, 5, 6, 7]
test_sum = sum_elements(test_list)
print(test_sum)
print(sum_el_2(test_list))
