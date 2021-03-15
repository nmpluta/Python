# -*- coding: utf-8 -*-
# L36 Napisać funkcję, która wyróżni kolorami czerwonym i zielonym odpowiednio największa
# i najmniejszą liczbę w danym łańcuchu. (html: x ) Zasady podobne jak w L34 Przykład:
# in: '1 dzielone przez 8 daje 0.128 a 7 dzielone przez 2 daje 3.5'
# out: '1 dzielone przez 8 daje 0.128 a 7 dzielone przez 2 daje 3.5'

def l36(string):
    string = string.split()
    _ = list(filter(lambda x: x.replace(".", "", 1).isdigit(), string))
    min_num = min(_)
    max_num = max(_)
    r = []
    for e in string:
        if e == min_num:
            r.append(f"<font color=green>{e}</font>")
        elif e == max_num:
            r.append(f"<font color=red>{e}</font>")
        else:
            r.append(e)
    return " ".join(r)


test = '1 dzielone przez 8 daje 0.128 a 7 dzielone przez 2 daje 3.5'
print(l36(test))