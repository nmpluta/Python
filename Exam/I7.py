# -*- coding: utf-8 -*-
# I7. doda "*" na początek linii zawierającej
# 	a) łańcuch "err".
# 	b) oddzielny wyraz 'error' (niewrażliwe na wielkiśc liter).
# 	c) przynajmniej jedną liczbę odzieloną spacjami (użyć wyjątku).

import re

def i7(string):
    return bool(re.search(r'(err)|(\b[Ee][Rr]{2}[Oo][Rr]\b)|(\b\d+\b)', string))


print(i7("Strin jakis tam eRror1 12 epor"))