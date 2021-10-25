with open('input.txt', 'r') as in_file:
    file = in_file.read().split('\n')
    n = int(file[0])
    x = sorted(map(int, file[1].split()))

with open('output.txt', 'w') as out_file:
    out_file.write(str(x[-1] * x[-2]))
