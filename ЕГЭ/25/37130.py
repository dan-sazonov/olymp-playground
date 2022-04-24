def find_divs(n):
    for i in range(17, n//2+1):
        if i %10==7 and n % i == 0:
            return i
    return 0

i  = 600_001
while True:
    d = find_divs(i)
    if d:
        print(i, d)
    i += 1