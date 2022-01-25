with open('input.txt') as open_read:
    n = int(open_read.read())

square = 1
ans = 0

while n > square:
    n -= square ** 2
    square += 1
    ans += 1 if n > 0 else 0

with open('output.txt', 'w') as open_write:
    open_write.write(str(ans))
