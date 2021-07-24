ans = 0

while True:
    n = int(input())
    if not n:
        break
    if n % 7 == 0 and n % 10 == 3:
        ans += n

print(ans)
