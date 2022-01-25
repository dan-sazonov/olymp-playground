from math import sqrt

with open('input.txt') as f_read:
    k_in = int(f_read.read())

n = 0
k = k_in

while n < k_in:
    # так как ограничения по времени нет, проверяем первые k членов последовательности
    k += 2 * (n + 1) - 1
    n += 1
    if sqrt(abs(k)).is_integer():
        out = int(sqrt(abs(k)))
        break
else:
    out = 'none'

with open('output.txt', 'w') as f_write:
    f_write.write(str(out))
    print(out)
