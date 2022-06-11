# НАЧАЛО
# ПОКА нашлось (111)
#     заменить (111, 2)
#     заменить (222, 11)
# КОНЕЦ ПОКА
# КОНЕЦ


def f(n):
    while '111' in n:
        n = n.replace('111', '2', 1)
        n = n.replace('222', '11', 1)
    return n


for i in range(10):
    s = '1' * 60 + '1' * i
    # print(i, len(s))
    if f(s) == '2211':
        print(60 + i)
