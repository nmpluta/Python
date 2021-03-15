# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:41:24 2021

@author: User
"""


def f03_13_printRectangle(a, b):
    """
    Prints the rectangle of a given size, using ASCII characters.
    Example:
3,5 -> 
+-+
| |
| |
| |
+-+

5,3 -> 
+---+
|   |
+---+

    Parameters
    ----------
    a : int
        Rectangle size in x.
    b : int
        Rectangle size in y.

    Returns
    -------
    None.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 84
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    d = a - 2

    def _():
        print('+%s+' % ('-' * d))

    _()
    for i in range(b - 2):
        print('|%s|' % (' ' * d))
    _()


f03_13_printRectangle(5, 4)
