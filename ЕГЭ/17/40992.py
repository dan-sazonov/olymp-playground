# arr = (8, 10, 2, 9, 5)
arr = list(map(int, open('40992.txt')))

avr = 0
k = 0
for j in arr:
    if j % 2 != 0:
        avr += j
        k += 1

avr /= k
c = 0
m = 0

for i in range(len(arr) - 1):
    x, y = arr[i], arr[i + 1]
    if (x % 5 == 0 or y % 5 == 0) and (x < avr or y < avr):
        c += 1
        m = max(m, x + y)

print(c, m)
