# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:41:46 2020

@author: Robert Szczygieł
"""

def stringMod(string):
    string = str.strip(string)
    string = string.lower()
    string = string.capitalize()
    if string[0] == 'B' or string[0] == 'b':
        string = 'H' + string[1:]
    string = string.replace(' ','-')
    string = string[:-1] + '!'
    return string

# Testing - OK
# oldString = "\n    BO STam    ahHA HAhaTT \t \n"
# print(oldString)
# newString = stringMod(oldString)
# print(newString, end='')

"""
Modifies the input string in the following way:
    - removes all the white characters from the beginning and the end of the string
    - first (non-white) character should be uppercase
    - if the first character is "B" or "b", it should be converted to "H"
    - all other characters should be lowercase
    - all spaces in the string should be replaced with '-' (minus) sings
    - last character should be replaced with "!"

Parameters
-------
arg : string

Returns
-------
Modified string

"""
