# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:46:52 2020

@author: User
"""


def listCross2(l1, l2):
    output_list = []
    for el_l1 in l1:
        for el_l2 in l2:
            if el_l1[:2] == el_l2[:2]:                      # [:2] two first letters - match
                output_list.append(el_l2)                   # appending words with a match to output list
                output_list.append(el_l1)
    output_list = list(dict.fromkeys(output_list))          # deleting duplicates from output_list
    output_list.sort()
    output_list.reverse()
    return output_list


# TESTING
# l1 = ['Anna', 'Monika', 'Marek', 'Janusz', 'Aniela']
# l2 = ['Gabriela', 'Marta', 'Maria', 'Antonina']
#
# test = listCross2(l1, l2)
# print(test)


"""
Returns sorted list of the words which begin with the same 
characters, common for two lists.

Parameters
----------
l1 : list of strings
l2 : list of strings
    
Returns
-------
Reversely sorted, unique list of words from the lists, that have the 
corresponding words beginning with the same two letters in another 
list, e.g.:
    l1 = ['Anna','Monika', 'Marek', 'Janusz', 'Aniela']
    l2 = ['Gabriela', 'Marta', 'Maria','Antonina']
    -> ['Marta', 'Marek', 'Maria', 'Antonina', 'Anna', 'Aniela']
"""
