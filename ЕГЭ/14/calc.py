def calc(num, base, to_base):
    num = int(str(num), base)
    ans = ''

    while num > 0:
        ans += str(num % to_base)
        num //= to_base
    return ans[::-1]


print(calc(4, 10, 2))
