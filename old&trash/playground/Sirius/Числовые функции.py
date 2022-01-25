n = int(input())
sigma_0 = sigma_1 = 0

for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0 and d != n ** 0.5:
        sigma_0 += 2
        sigma_1 += n // d + d
    elif n % d == 0 and d == n ** 0.5:
        sigma_0 += 1
        sigma_1 += d

print(sigma_0, sigma_1)
