def find_m(n):
    ans = 0
    c = 0
    for i in range(n//2+2, 1, -1):
        if n % i == 0:
            ans += i
            c += 1
        if c == 2:
            break
    return ans if c == 2 else 0

print(find_m(50))
i = 10_000_001
while True:
    m = find_m(i)
    if 0 < m < 10_000:
        print(m)
