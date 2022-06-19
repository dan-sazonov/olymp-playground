arr = list(map(int, open('37355.txt')))
c = 0
m = 0

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr) - 1):
        if (arr[i] + arr[j]) % 7 == 0:
            c += 1
            m = max(m, (arr[i] + arr[j]))

print(c, m)
