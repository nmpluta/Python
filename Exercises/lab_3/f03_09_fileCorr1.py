# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:17:58 2021

@author: User
"""
from re import sub as r

def f03_09_fileCorr1(f):
    """
    Prints the file, correcting spaces. The corrections are:
        - remove leading and trailing spaces from each line
        - remove spaces before comma and point (, .)
        - adding spaces, if necessary, after comma and point;
          there should be one space after each comma and point
          (not at the end of the line)

    Parameters
    ----------
    f : str
        Input file name

    Returns
    -------
    None.
    
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 152
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "re" module
    - hint: check the documentation:
      https://docs.python.org/3/library/re.html

    """
    # # Overwriting the file!
    with open(f, 'r+') as p:
        d = p.read()
        p.seek(0)
        d = r(r"\.", ". ", d)
        d = r(r",", ", ", d)
        d = r(r"^\s+|\s+$", "", d)  # Trzeba bedzie uzyc Lookahead Assertions
        d = r(r" +", " ", d)
        d = r(r"\s+,", ",", d)
        d = r(r"\s+\.", ".", d)
        print(r(r"\s+\n\s+", r"\n", d))
        p.truncate()


# from re import sub as s
# with open(f) as p:
#     print(s(r"\s+\n\s+", r"\n", s(r"\s+\.", ".", s(r"\s+,", ",", s(r" +", " ",
#             s(r"^\s+|\s+$", "", s(r",", ", ", s(r"\.", ". ", p.read()))))))))

# import re
# # Overwriting the file!
# with open(f, 'r+') as p:
#     d = p.read()
#     p.seek(0)
#     d = re.sub(r"\.", ". ", d)
#     d = re.sub(r",", ", ", d)
#     d = re.sub(r"^\s+|\s+$", "", d)  # Trzeba bedzie uzyc Lookahead Assertions
#     d = re.sub(r" +", " ", d)
#     d = re.sub(r"\s+,", ",", d)
#     d = re.sub(r"\s+\.", ".", d)
#     print(re.sub(r"\s+\n\s+", r"\n", d))
#     p.truncate()


# Testing
f03_09_fileCorr1("text_file.txt")

#     # Overwriting the file!
#     with open(f, 'r+') as p:
#         d = p.read()
#         p.seek(0)
#         d = re.sub(r"^\s+|\s+$", "", d)                 # Trzeba bedzie uzyc Lookahead Assertions
#         d = re.sub(r"\s+", " ", d)
#         d = re.sub(r"\s+,", ",", d)
#         d = re.sub(r"\s+\.", ".", d)
#         print(re.sub(r"\n\s+", r"\n", d), end='')
#         p.truncate()
#
#
# # Testing
# # f03_09_fileCorr1("text_file.txt")

# # Overwriting the file!
# with open(f, 'r+') as p:
#     d = p.read()
#     p.seek(0)
#     d = re.sub(r"^\s+|\s+$", "", d)  # Trzeba bedzie uzyc Lookahead Assertions
#     d = re.sub(r"\s+", " ", d)
#     d = re.sub(r"\s+,", ",", d)
#     d = re.sub(r"\s+\.", ".", d)
#     p.write(re.sub(r"\n\s+", r"\n", d))
#     p.truncate()
