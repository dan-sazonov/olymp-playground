with open('input.txt') as file_read:
    line = list(map(int, file_read.read().split('\n')))
    l = line[0]
    r = line[1]
    a = line[2]
counter = 0

for i in range(l, r + 1):
    for j in range(i, r + 1):
        if l <= i < j <= r and (j - i) % a == 0:
            counter += 1

with open('output.txt', 'w') as file_write:
    file_write.write(str(counter))
    # print(counter)
