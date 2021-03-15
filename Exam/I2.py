# -*- coding: utf-8 -*-
# I2. zwróci iloczyn logiczny dwóch ciągów zerojedynkowych
#    in:  a: '001101010'
#         b: '101001100'
#    out: c: '001001000'

# supp. function
def _convert_to_binary_list(string):
    lst_char_digits = list(filter(lambda e: e.isdigit(), string))
    return [int(e) for e in lst_char_digits]


# main
def i2(a, b):
    a = _convert_to_binary_list(a)
    b = _convert_to_binary_list(b)
    r = [str(ea * eb) for (ea, eb) in zip(a, b)]
    return "".join(r)


a_t = '001101010'
b_t = '101001100'
test_i2 = i2(a_t, b_t)
print(f"Test i2 is {test_i2 == '001001000'}, value returned: {test_i2}")
