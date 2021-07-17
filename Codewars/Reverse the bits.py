def reverse_bits(n):
    return int(str(bin(n))[:1:-1], base=2)


print(reverse_bits(417))
