base = int(input())


def kaprekar(base_number, iter):
    if base_number == 6174:
        return iter
    elif str(base_number) == str(base_number)[::-1]:
        return 'Invalid input'
    else:
        iter += 1
        a = sorted(str(base_number))
        b = a[::-1]
        return kaprekar(int(''.join(b)) - int(''.join(a)), iter)


print('Amount of iterations:', kaprekar(base, 0) if 6174 >= base > 1000 and base % 1111 != 0 else 'Invalid input')
