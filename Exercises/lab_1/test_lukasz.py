def f02_07_findCommonEls2(a,b):
    l = [i for i in a if i in b]
    return l


# TEST
a = [99999, 6, 5, 4, 3, 2, 1, -99999]
b = [99999, 6, 5, 4, -2, -3, -7, -99999]

print(f02_07_findCommonEls2(a, b))