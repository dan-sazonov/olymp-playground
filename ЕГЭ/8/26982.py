c = 0

for i in range(100_000, 999_999+1, 5):
    s = tuple(map(int, str(i)))
    flag = 1
    for j in range(6-1):
        if ((s[j] % 2) + (s[j+1] % 2) != 1) or s.count(s[j]) > 1:
            flag = 0
    c += flag

print(c)
