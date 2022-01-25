n = int(input())
a = [1]

for i in range(1, n + 1):
    a.append(i + a[i - 1])

print(a[n])
