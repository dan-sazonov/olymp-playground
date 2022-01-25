with open('input.txt') as file_read:
    line = tuple(map(int, file_read.read().split('\n')))
    a, b, c, = line
counter = 0

while a < b:
    a += 2 if (a + 2) % c != 0 and a + 2 <= b and a < b else 1
    counter += 1

print(counter)