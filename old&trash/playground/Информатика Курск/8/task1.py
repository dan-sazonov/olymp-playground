# на 70 баллов, полный бал - 111951 в информатиксе
# решение понял
n = int(input())
k = int(input())
ans = 0

while k * 3 != n:
    k += 1
    n += 1
    ans += 1

print(ans)
