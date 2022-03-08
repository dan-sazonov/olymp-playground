arr = list(map(int, open('17-5.txt').readlines()))
count = 0
m = -200

for i in range(len(arr)):
    if arr[i] % 10 == 5 and arr[i + 1] % 10 == 5:
        count += 1
        m = max(m, arr[i] + arr[i + 1])

print(count, m)
