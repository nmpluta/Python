# -*- coding: utf-8 -*-
# D16 zamieni wyrazy na liście na wyrazy ze słownika, jeżeli danego wyrazu nie ma w słowniku
# to powinien zastąpić litery kropkami.

def d16(lst, dic):
    return [dic.get(string, "."*len(string)) for string in lst]


lst_1 = ["second", "word", "to", "change", "start"]
dic_1 = {"second": "first", "word": "test", "start": "end"}
print(d16(lst_1, dic_1))
