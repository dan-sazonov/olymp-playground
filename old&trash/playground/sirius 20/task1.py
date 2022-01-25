a = int(input())
n = int(input())
res = 0

if n > 0 > a and a + n > 0:
    res = a + n + 1
elif a > 0 > n and a + n < 0:
    res = a + n - 1
elif n > 0 > a and a + n == 0:
    res = 1
elif a > 0 > n and a + n == 0:
    res = -1
else:
    res = a + n

print(res)
