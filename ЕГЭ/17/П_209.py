arr = list(map(int, open('17-205.txt').readlines()))
count = 0
m = -20001

for i in range(len(arr) - 1):
    if (arr[i] % 7 == 0 or arr[i + 1] % 7 == 0) and abs(arr[i] + arr[i + 1]) % 100 == 19:
        count += 1
        m = max(m, arr[i] + arr[i + 1])

print(count, m)
