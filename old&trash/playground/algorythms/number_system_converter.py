def convert(x, q, a):
    """
    x - начальное число, q - куда переводим, a - откуда переводим
    """
    if isinstance(x, str):
        x = int(x, a)
    else:
        x = int(x)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x < q:
        return alphabet[x]
    else:
        return convert(x // q, q, a) + alphabet[x % q]


print(convert('AA16342F', 8, 16))
# 25205432057
