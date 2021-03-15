# -*- coding: utf-8 -*-
# L26 (63) wstawi dany łańcuch na początki wszystkich początki wszstkich łańcuchów na liście.

def l26(beg_str, lst):
    return [beg_str + string for string in lst]


print(l26("ABC", ["alala", "drugi", "   trzeci"]))
