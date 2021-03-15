# -*- coding: utf-8 -*-
# I3. wykryje warunek startu i stopu na magistrali I2C.
#    in: sda: '1100 0011'
#        scl: '1111 1111'
#        out: '--s- --t-

def i3(sda, scl):
    flag = 0  # 0 - Stop --> Start, 1 - Start --> Stop
    r = []
    for (num_1, num_2) in zip(sda, scl):
        if num_1.isdigit() and num_2.isdigit():
            if int(num_1) * int(num_2) == 0 and flag == 0:
                flag = 1
                r.append('s')
            elif int(num_1) * int(num_2) == 1 and flag == 1:
                flag = 0
                r.append('t')
            else:
                r.append('-')
        else:
            r.append(' ')
    return "".join(r)


# Testing
sda_t = '1100 0011'
scl_t = '1111 1111'
test_i3 = i3(sda_t, scl_t)
print(f"Test i3 is {test_i3 == '--s- --t-'}, value returned: {test_i3}")
