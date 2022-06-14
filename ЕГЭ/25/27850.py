def is_prime(n):
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    return True


arr = range(245690, 245757)
for i in range(len(arr)):
    if is_prime(arr[i]):
        print(i + 1, arr[i])
