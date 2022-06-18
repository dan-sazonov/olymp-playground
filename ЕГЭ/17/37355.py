arr = list(map(int, open('37355.txt')))
c = 0
m = 0

for i in range(len(arr) - 1):
    for j in range(i, len(arr) - 1):
        if (arr[i] + arr[i+1]) % 7 == 0:
            c += 1
            m = max(m, (arr[i] + arr[i+1]))

c += 1
m = max(m, (arr[i] + arr[i+1]))

print(c, m)
