with open('input.txt', 'r') as in_file:
    file = in_file.read().split('\n')
    n = int(file[0])
    m = list(map(int, file[1].split()))

max_val = 0

for i in range(1, n - 1):
    for j in range(i + 1, n):
        if m[i] == m[j] and j - i > max_val:
            max_val = j - i
            break

with open('output.txt', 'w') as out_file:
    out_file.write(str(max_val))
