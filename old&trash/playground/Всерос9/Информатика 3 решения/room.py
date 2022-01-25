with open('input.txt') as file_read:
    input = map(int, file_read.read().split('\n'))
    w, l, h = input
if (min(w, l) / h >= 2) and (max(w, l) / min(w, l) <= 2):
    out = 'good'
else:
    out = 'bad'
with open('output.txt', 'w') as file_write:
    file_write.write(out)
