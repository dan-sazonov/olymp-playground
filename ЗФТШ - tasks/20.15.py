ans = 0

while True:
    n = int(input())
    if n == 0:
        break

    if n // 100 < 10 and n % 3 == 0 and n % 10 == 7:
        ans += n

print(n)
