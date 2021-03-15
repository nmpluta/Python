# -*- coding: utf-8 -*-
# I1. Napisać funkcję, która:
#   a) policzy liczbę zboczy w ciągu zerojedynkowym
#      in: '01011001', out: 5
#   b) wyznaczy miejsca wszystkich zboczy
#      in: '00111000100001'
# 	 out:'--*--*--**---*'
#   c) wyznaczy miejsca zboczy rosnących
#      in: '001110100001'
# 	 out:'--r---r----r'
#   d) doda do (c) oznaczenie okresu o najwiekszej amplitudzie
#      okresy należy liczyć jako liczba cyfr między zboczami rosnącymi
#      in: '0011101000011010'
# 	 out:'--r---r----x--r-'
#   e) wyliczy średni okres przebiegu
#      in: '001110100001'
# 	 out: 4.5 ((4+5)/2) \\ okres
#   f) wyliczy odchylenie standardowe okresów przebiegu


def i1a(string):
    count = 0
    for index in range(len(string) - 1):
        if string[index] == '0' and string[index + 1] == '1':               # rising edge
            count += 1
        elif string[index] == '1' and string[index + 1] == '0':             # trailing edge
            count += 1
    return count


def i1b(string):
    result = []
    temp = '0' + string
    for index in range(1, len(string) + 1, 1):
        if temp[index] == '1' and temp[index - 1] == '0':               # rising edge
            result.append('*')
        elif temp[index] == '0' and temp[index - 1] == '1':             # trailing edge
            result.append('*')
        else:
            result.append('-')
    return "".join(result)


def i1c(string):
    result = []
    temp = '0' + string
    for index in range(1, len(string) + 1, 1):
        if temp[index] == '1' and temp[index - 1] == '0':               # rising edge
            result.append('r')
        else:
            result.append('-')
    return "".join(result)


def i1d(string):
    result = []
    max_ampl = 0
    _ = 0
    temp = '0' + string
    for index in range(1, len(string) + 1, 1):
        if temp[index] == '1' and temp[index - 1] == '0':               # rising edge
            if _ > max_ampl:
                max_ampl = _
                max_index = index - 1
            result.append('r')
            _ = 0
        else:
            result.append('-')
            _ += 1
    result[max_index] = 'x'
    return "".join(result)


# Testing
test_i1a = i1a('01011001')
print(f"Test i1a is {test_i1a == 5}, value returned: {test_i1a}")

test_i1b = i1b('00111000100001')
print(f"Test i1b is {test_i1b == '--*--*--**---*'}, value returned: {test_i1b}")

test_i1c = i1c('001110100001')
print(f"Test i1c is {test_i1c == '--r---r----r'}, value returned: {test_i1c}")

test_i1d = i1d('0011101000011010')
print(f"Test i1d is {test_i1d == '--r---r----x--r-'}, value returned: {test_i1d}")


