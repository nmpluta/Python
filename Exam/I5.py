# -*- coding: utf-8 -*-
# I5. przy uzyciu spacaji wyrówna do prawej łańcuch znaków skłądający się z wielu linii.

test = " Testujemy taka funkcje,\n" \
       "co ma sobie wyrownywac do prawej.\n" \
       "Zobaczymy zaraz czy działa?\n" \
       "Udało się?"


def i5(string):
    sentences = string.split('\n')
    result = []
    max_len = max([len(sentence) for sentence in sentences])
    for sentence in sentences:
        diff_len = max_len - len(sentence)
        result.append(' '*diff_len + sentence)
    return "\n".join(result)


print(i5(test))
