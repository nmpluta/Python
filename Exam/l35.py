# -*- coding: utf-8 -*-
# L35 Napisać funkcję, która ograniczy liczbę miejsc po przecinku w liczbach do liczby o najmniejszej precyzji.
# Przykłąd: in: 'ala 1.23456 ma 12.3456 kota 123.456' out: 'ala 1.234 ma 12.345 kota 123.456'


def l35(string):
    string = string.split()
    # m = 20
    # for e in string:
    #     if e.replace(".", "", 1).isdigit():
    #         m = min(m, len(e.split('.')[1]))

    _ = list(filter(lambda x: x.replace(".", "", 1).isdigit(), string))
    m = min(map(lambda x: len(x.split('.')[1]), _))

    r = []
    for e in string:
        if e.replace(".", "", 1).isdigit():
            (whole, fraction) = e.split('.')
            r.append(whole + '.' + fraction[:m])
        else:
            r.append(e)

    r = " ".join(r)
    return r


test = 'ala 1.23456 ma 12.3456 kota 123.456'
print(l35(test))
