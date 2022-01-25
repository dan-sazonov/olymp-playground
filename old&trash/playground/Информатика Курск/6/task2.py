# wa
n = int(input())
s = list(map(int, input().split())) + [0, 0]
ans = []
skip = False

if n > 3 and s[-3] == 10:
    n -= 2
elif n > 2 and s[-3] + s[-2] == 10:
    n -= 1

for i in range(n):
    if skip:
        continue
    if s[i] == 10:
        ans.append(s[i] + s[i + 1] + s[i + 2])
    elif s[i] + s[i + 1] == 10:
        ans.append(10 + s[i + 2])
        skip = True
    else:
        ans.append(s[i] + s[i + 1])
        skip = True
print(ans, sum(ans))
