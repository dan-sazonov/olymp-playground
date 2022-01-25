with open('../input.txt') as open_read:
    names = open_read.read().split()

for i in names:
    if names.count(i) == 1 and i.isalpha():
        break

with open('../output.txt', 'w') as open_write:
    open_write.write(i)
