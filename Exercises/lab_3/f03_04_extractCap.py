# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:25:30 2021

@author: User
"""
import re


def f03_04_extractCap(s):
    """
    The function returns the list of the words with the first letter
    capitalized (A-Z) in the input string

    Parameters
    ----------
    s : str
        Any string (can be empty)

    Returns
    -------
    list
        List of words in the string starting with A-Z
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 63
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "re" module
      https://www.w3schools.com/python/python_regex.asp
    """
    return re.findall('[A-Z]\w*', s)


# Testing
test_string = "You do like Rome. Why?"
print(f03_04_extractCap(test_string))


# return re.findall('[A-Z]\w*', re.sub('\W', ' ', s))