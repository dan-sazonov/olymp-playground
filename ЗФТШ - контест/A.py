with open('input.txt', 'r') as in_file:
    n, m, k = map(int, in_file.readline().split())

if m < k:
    ans = n * m
else:
    ans = ((k - 1) + int(m / k)) * n

with open('output.txt', 'w') as out_file:
    out_file.write(str(ans))
