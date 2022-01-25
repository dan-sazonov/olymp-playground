with open('input.txt') as file_read:
    years = int(file_read.read())
    assert (1 <= years <= 25)

credit = 100
sums = ['100']

for c in range(years - 1):
    credit *= 2
    length = len(str(credit)) / 2  # находим половину от кол-ва символов

    if length != int(length):
        length = int(length) + 1  # округляем в большую сторону, если есть дробная часть
    else:
        length = int(length)

    half_end = str(credit)[::-1][:length:]  # срезаем половину символов с конца

    if len(str(credit)) % 2 == 0:  # срезаем половину символов с начала
        half_start = str(credit)[:length:]
    else:
        half_start = str(credit)[:length - 1:]

    if int(half_end) == 0:
        sums.append(str(credit))
    else:
        sums.append(str(int(half_start) + 1) + (
                    '0' * len(half_end)))  # увеличиваем первую половину на разряд, если во второй были не только нули

with open('output.txt', 'w') as file_write:
    file_write.write('\n'.join(sums))
