# -*- coding: utf-8 -*-
# D5 (56) dla liczb on 1 do danej (N) wygeneruje słownik
# w którym kluczem będzie wartość liczby a wartością jej kwadrat.

def d5(N):
    return {i: i*i for i in range(1, 1+N)}


print(d5(5))
print(d5(9))
