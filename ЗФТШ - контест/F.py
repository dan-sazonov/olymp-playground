with open('input.txt', 'r') as in_file:
    m = int(in_file.readline())

with open('output.txt', 'w') as out_file:
    out_file.write(str(int(f'0b{bin(m)[::-1].rstrip("b0")}', base=2)))
