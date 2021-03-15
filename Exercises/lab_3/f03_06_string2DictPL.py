# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:32:24 2021

@author: User
"""
import locale as l


def f03_06_string2DictPL(s):
    """
    The function counts the occurrences of the characters in the string
    and returns the sorted dictionary where the key is a character and 
    the value is the number of occurrences.

    Parameters
    ----------
    s : str
        Any string (can by empty).

    Returns
    -------
    dict
        The keys of the dictionary are the chars from the string. The
        value is the number of the occurrences of the char in the string.
        The dictionary is sorted by keys in the ascending order, according
        to the Polish language rules. Sort order:
            a A ą Ą b B c C ć Ć d D ...
        The encoding used is UTF-8
        
   Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 131
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "locale" module
    """
    l.setlocale(l.LC_COLLATE, "pl_PL.UTF-8")
    print(sorted(s, key=l.strxfrm))
    return {c: s.count(c) for c in sorted(s, key=l.strxfrm)}


#Testing
print(f03_06_string2DictPL("Natalia Pluta"))

# count={}
# >>> for c in str1:
# ...    count[c]=count.setdefault(c, 0)+1

# a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# d = {e: s.count(e) for e in set(s) if e in a}
# return d


# a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# d = {e:s.count(e) for e in set(s) if e in a}
# return d
