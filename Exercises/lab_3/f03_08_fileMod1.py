# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:43:13 2021

@author: User
"""
import re


def f03_08_fileMod1(f, a, b):
    """
    Prints the text from a file with replaced words.
    Only full words are replaced.
    The replacement is case-insensitive.

    Parameters
    ----------
    f : str
        Name of the file to open.
    a : str
        Word in the text to be replaced
    b : str
        Replacement for the word.

    Returns
    -------
    None.
    
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 100
      (docstring and comments are ignored when counting)
    - use "import" once
    - remember to close the file after reading
    - note on closing the files:
      https://www.geeksforgeeks.org/with-statement-in-python/
    """
    with open(f) as p:
        print(re.sub(rf'\b{a}\b', b, p.read(), flags=re.I), end='')



# TESTING
f03_08_fileMod1('text_file.txt', 'slowa', 'tekst')
f03_08_fileMod1('text_file_2.txt', 'Ala', 'XXX')

# with open(f, 'r') as p:
#     d = p.read()
#     p.close()
#     print(re.sub(rf"\b{a}\b", b, d, re.I), end='')


# Overwriting the file!
# with open(f, 'r+') as p:
#     d = p.read()
#     p.seek(0)
#     p.write(d.replace(a, b))
#     p.truncate()
