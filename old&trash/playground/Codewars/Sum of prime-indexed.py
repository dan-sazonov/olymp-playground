def total(arr):
    if not arr:
        return 0

    result = 0
    sieve = list(range(len(arr)))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0

    for c in set(sieve):
        if c:
            result += arr[c]

    return result
