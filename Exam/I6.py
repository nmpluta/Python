# -*- coding: utf-8 -*-
# I6. usunie puste linie z łańcucha znaków skłądający się z wielu linii.

test = " Testujemy taka funkcje,\n" \
       "co ma usuwac puste linie.\n" \
       "\n" \
       "Takie jak ta powyzej i ponizej\n" \
       "           \n" \
       "        \n" \
       "Zobaczymy zaraz czy działa?\n" \
       "Udało się?"


def i6(string):
    sentences = string.split('\n')
    result = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            result.append(sentence)
    return "\n".join(result)


print(i6(test))
