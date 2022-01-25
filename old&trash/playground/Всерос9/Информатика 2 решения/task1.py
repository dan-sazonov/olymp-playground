with open('input.txt') as f_read:
    values = list(map(int, f_read.read().split('\n')))
    m, x, y, w, h = values[0], values[1], values[2], values[3], values[4]

width = w // m + (1 if x % m != 0 else 0)
height = h // m + (1 if y % m != 0 else 0)

with open('output.txt', 'w') as f_write:
    f_write.write(str(width * height))