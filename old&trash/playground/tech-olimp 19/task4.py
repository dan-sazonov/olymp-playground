a = int(input())
b = int(input())
fl1 = '0'
fl2 = '0'
fl3 = '0'
a1_1 = a + 3
b1_1 = b
a1_2 = a
b1_2 = b + 2
a1_3 = a
b1_3 = b + 4
if ((a1_1 ** 2) + (b1_1 ** 2)) > 144:
    fl1 = 'true'
if ((a1_2 ** 2) + (b1_2 ** 2)) > 144:
    fl2 = 'true'
if ((a1_3 ** 2) + (b1_3 ** 2)) > 144:
    fl3 = 'true'
print(a1_1, '|', b1_1, '|', fl1)
print(a1_2, '|', b1_2, '|', fl2)
print(a1_3, '|', b1_3, '|', fl3)