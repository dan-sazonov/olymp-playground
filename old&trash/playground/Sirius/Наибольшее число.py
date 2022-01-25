s = input()
numbers = [int(i) for i in s if i.isdigit()]

cnt = [0] * 10
for i in numbers:
    cnt[i] += 1
a = []
for j in range(len(cnt)):
    a += [j] * cnt[j]
print(*reversed(a), sep='')
