arr = list(map(int, open('17-274.txt')))
c = 0
m = 20001

for i in range(len(arr) - 1):
    if (abs(arr[i]) + abs(arr[i + 1]) > 17043) and (abs(arr[i]) + abs(arr[i + 1])) % 3 == 0:
        c += 1
        m = min(m, arr[i] + arr[i + 1])

print(c, m)
