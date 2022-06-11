# НАЧАЛО
#
# ПОКА нашлось (12)
#
#     заменить (12, 4)
#
# КОНЕЦ ПОКА
#
# КОНЕЦ

s = '1' * 10
min2 = 100000

for i in range(30):
    s += '2' * i
    n = sum(map(int, s))
    print(n)
    if n == 25:
        print(i)

print(min2)
