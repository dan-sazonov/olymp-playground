arr = list(map(int, open('17-7.txt').readlines()))
count = 0
m = 0

for i in range(len(arr) - 2):
    if sum((arr[i] % 16 == 0, arr[i + 1] % 16 == 0, arr[i + 2] % 16 == 0)) >= 2:
        count += 1
        m += max(arr[i], arr[i + 1], arr[i + 2])

print(count, m)
