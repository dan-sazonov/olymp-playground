with open('input.txt') as open_read:
    input = list(map(int, open_read.read().split()))
    x = input[0]
    max_base = input[1] + 1
out = []


def convert(number, base):
    converted = []
    while True:
        converted.append(number % base)
        number //= base
        if number < base:
            converted.append(number)
            break
    converted.reverse()
    return list(str(''.join(map(str, converted))).lstrip('0'))


for i in range(2, max_base):
    converted_number = convert(x, i)
    reversed_number = list(reversed(converted_number))
    if converted_number == reversed_number and len(converted_number) > 1:
        out.append(str(i))

with open('output.txt', 'w') as open_write:
    open_write.write(' '.join(out) if out else '0')
