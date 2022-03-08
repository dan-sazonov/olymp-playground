arr = list(map(int, open('17-199.txt').readlines()))
count = 0
m = -20001


def f(x):
    return 10 <= x <= 99 and x % 2 == 0


for i in range(len(arr) - 2):
    if not f(arr[i]) and f(arr[i + 1]) and not f(arr[i + 2]):
        m = max(m, sum(arr[i:i+3]))
        count += 1

print(count, m)
