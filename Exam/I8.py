# -*- coding: utf-8 -*-
# I8. usunie z łańcucha wszystkie wielokrotne spacje.

def i8(string):
    words = string.split(' ')
    return ' '.join([word.strip(' ') for word in words if word.strip() != ''])


# Testing
test = "Some   words  with    tooo many spaces... \n" \
       "I'm gonna    remove them now!   \n" \
       "Is   it working?"

print(i8(test))
