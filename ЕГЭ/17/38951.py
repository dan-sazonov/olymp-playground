arr = list(map(int, open('38951.txt')))
c = 0
m = 0

for i in range(len(arr) - 1):
    if (arr[i] % 3 == 0 or arr[i+1] % 3 == 0) and (arr[i] + arr[i+1]) %5 == 0:
        c += 1
        m = max(m, arr[i] + arr[i+1])

m = max(m, arr[i] + arr[i+1])
print(c, m)
