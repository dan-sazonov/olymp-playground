q = int(input())
x = int(input())


def convert(num, base):
    alphabet = '0123456789'
    if num < base:
        return alphabet[num]
    else:
        return convert(num // base, base) + alphabet[num % base]


print(convert(x, q))
