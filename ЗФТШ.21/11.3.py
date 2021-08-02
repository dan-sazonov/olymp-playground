# Способ 1. Брутфорс. Используя библиотечную функцию, создаем сочетания с повторениями элементов от 0 до n длины n.
# Затем, мы вычисляем сумму элементов в каждом сочетании, и если она кратна (n+1), выводим. Асимптотика этого решения
# будет превышать O(n^2), но учитывая небольшое маскимальное значение n, оно приемлимо.
# Способ 2. ???

from itertools import combinations_with_replacement as cwr

n = int(input())
arr = range(0, n + 1)

for i in cwr(arr, n):
    if sum(i) % (n + 1) == 0:
        print(i)

# def calcsum(s, idx, maxx, n, a):
#     if idx > n:
#         return
#     if s == 0:
#         # print(a +[0]*(n-idx))
#         ans.append(a +[0]*(n-idx))
#         return
#     for i in range(maxx, 0, -1):
#         calcsum(s - i, idx + 1, i, n, a + [i])
#
#
# def nsums(n):
#     for t in range(n * n  // (n + 1) + 1):
#         s = t * (n + 1)
#         calcsum(s, 0, n, n, [])
#
# nsums(12)
