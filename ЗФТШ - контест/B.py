with open('input.txt', 'r') as in_file:
    n, m, d, k = map(int, in_file.readline().split())

with open('output.txt', 'w') as out_file:
    out_file.write(str(((n + m) * d * k) - (d * d * n * m)))

# cout << ((n + m) * d * k) - (d * d * n * m);
