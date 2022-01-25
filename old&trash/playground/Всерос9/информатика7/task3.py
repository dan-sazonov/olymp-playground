a, b = int(input()), int(input())
n = 0

while True:
    n += 1
    if (n - 1) % a == 0 and (n + 1) % b == 0:
        print(n)
        break
