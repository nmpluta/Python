# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:46:52 2020

@author: User
"""


def listCross2(l1, l2):
    # length_l1 = len(l1)
    # length_l2 = len(l2)
    output_list = []
    # i = 0
    # while i < (length_l1-1):
    #     j = i + 1
    #     while j < length_l1:
    #         if l1[i][:2] == l1[j][:2]:          # [:2] two first letters - match
    #             output_list.append(l1[j])       # appending words with a match to output list
    #             del l1[j]                       # deleting words with a match from l1 list
    #             length_l1 = len(l1)
    #         else:
    #             j += 1
    #     i += 1

    for el_l1 in l1:
        flag = True
        for el_l2 in l2:
            if el_l1[:2] == el_l2[:2]:
                print(el_l1, el_l2)
                output_list.append(el_l2)
                if flag:
                    flag = False
                    output_list.append(el_l1)
    return output_list

    # for i in range(length_l1-1):
    #     for j in range(i+1, length_l1):
    #         if l1[i][:2] == l1[j][:2]:
    #             print(l1[i], l1[j])


# TESTING
l1 = ['Anna', 'Monika', 'Marek', 'Janusz', 'Aniela', 'Antonina']
l2 = ['Gabriela', 'Marta', 'Maria', 'Anabel', 'Jarek']

print(l1)
print(len(l1))
test = listCross2(l1, l2)
print(test)
print(len(test))


for l1_word in l1:
    if l1_word[:2] in l2:
        print(l1_word)

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
