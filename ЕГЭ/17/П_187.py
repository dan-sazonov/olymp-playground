arr = list(map(int, open('17-6.txt').readlines()))
count = 0
m = 0

for i in range(len(arr) - 2):
    if all((bin(arr[i]).count('1') == 3, bin(arr[i + 1]).count('1') == 3, bin(arr[i + 2]).count('1') == 3)):
        count += 1
        m += max(arr[i], arr[i + 1], arr[i + 2])

print(count, m)
