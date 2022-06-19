arr = list(map(int, open('17-243.txt')))
amn = 0
c = 0
m = 20001

for j in arr:
    if j % 33 == 0:
        amn += sum(map(int, str(j)))

for i in range(len(arr) - 1):
    if (arr[i] > amn) or (arr[i+1] > amn):
        c += 1
        m = min(m, arr[i] + arr[i+1])

print(c, m)
