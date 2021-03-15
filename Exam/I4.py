# -*- coding: utf-8 -*-
# I4.
# 	a. zmieni na duże pierwsze litery w zdaniach rozdzielonych kropkami.
# 	b. ustawi odpowiednią liczbę spacji przed i po przecinkach w zdaniu.


def i4(str):
    sentences = str.split('.')
    r = []
    for sentence in sentences:
        r.append(sentence.strip().capitalize())

    return ". ".join(r) + '.'


test = 'Testing function. Is it working .  What do you think'
print(i4(test))
