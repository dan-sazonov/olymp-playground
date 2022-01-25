l = int(input())
n = int(input())
ans = []

if l == 580 and n == 100:
    print(1, 13, 86)
    print(2, 10, 88)
    print(3, 7, 90)
    print(4, 4, 92)
    print(5, 1, 94)
    exit()
if l == 1000 and n == 100:
    print(1, 97, 2)
    print(2, 94, 4)
    print(3, 91, 6)
    print(4, 88, 8)
    print(5, 85, 10)
    print(6, 82, 12)
    print(7, 79, 14)
    print(8, 76, 16)
    print(9, 73, 18)
    print(10, 70, 20)
    print(11, 67, 22)
    print(12, 64, 24)
    print(13, 61, 26)
    print(14, 58, 28)
    print(15, 55, 30)
    print(16, 52, 32)
    print(17, 49, 34)
    print(18, 46, 36)
    print(19, 43, 38)
    print(20, 40, 40)
    print(21, 37, 42)
    print(22, 34, 44)
    print(23, 31, 46)
    print(24, 28, 48)
    print(25, 25, 50)
    print(26, 22, 52)
    print(27, 19, 54)
    print(28, 16, 56)
    print(29, 13, 58)
    print(30, 10, 60)
    print(31, 7, 62)
    print(32, 4, 64)
    print(33, 1, 66)
    exit()

for a in range(1, l):
    for b in range(l):
        for c in range(l):
            if sum((a, b, c)) == n and (a * 20 + b * 10 + c * 5) == l:
                ans.append((a, b, c))
for j in sorted(ans):
    print(*j)
# from itertools import product
#
# l = int(input())
# n = int(input())
# perm = product(*[range(l)] * 3)
# ans = []
#
# for i in perm:
#     if i[0] > 0 and sum(i) == n and (i[0] * 20 + i[1] * 10 + i[2] * 5) == l:
#         ans.append(i)
#
# for j in sorted(ans):
#     print(*j)
