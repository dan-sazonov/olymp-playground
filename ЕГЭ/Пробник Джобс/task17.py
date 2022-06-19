arr = list(map(int, open('17.txt')))
avr = 1000000
c = 0
m = 0

for i in arr:
    if i % 17 == 0:
        avr = min(i, avr)

for j in range(len(arr) - 1):
    if (arr[j] % avr == 0) or (arr[j + 1] % avr == 0):
        c += 1
        m = max(m, arr[j] + arr[j + 1])

print(c, m)
