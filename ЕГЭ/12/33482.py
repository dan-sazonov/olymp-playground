# НАЧАЛО
#
#     ПОКА
# нашлось(111)
#
#         заменить(111, 22)
#
#         заменить(222, 11)
#
#     КОНЕЦ
# ПОКА
#
# КОНЕЦ
#


def foo(n):
    s = '1' * n
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    return s.count('1')


n = 100
ans = []
while n < 1000:
    tmp = (n, foo(n))
    ans.append(tmp)
    n += 1

ans.sort(key=lambda x: x[1])
print(*ans, sep='\n')
