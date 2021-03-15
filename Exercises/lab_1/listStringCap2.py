# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:12:12 2020

@author: User
"""


def listStringCap2(li):
    list_length = len(li)
    for i in range(list_length):
        word_length = len(li[i])
        if word_length >= 2:
            li[i] = li[i][0].capitalize() + li[i][1].capitalize() + li[i][2:]
        elif word_length == 1:
            li[i] = li[i].capitalize()
    return li


#TESTING - OK
# list1 = ["ala", "kot", "pies", "test", "ok", "kl", "t", ""]
# test1 = listStringCap2(list1)
# print(test1)

"""
Capitalize two first characters of each word in the list.

Parameters
----------
li : list of string. Note: strings may be empty.

Returns
-------
The list, where all the words have first two characters capitalized.

"""
