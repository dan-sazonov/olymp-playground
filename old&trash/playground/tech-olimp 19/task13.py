def isprime(n):
    i = 2
    j = 0
    while (True):
        if (i * i <= n) and (j != 1):
            if (n % i) == 0:
                j = j + 1
            i = i + 1
        elif j == 1:
            return False
        else:
            return True

ans = 0
for c in range(1, 2020):
    if (isprime(c)) and ((2019 % c) == 29):
        ans += 1
    else:
        continue
print(ans)