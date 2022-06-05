# всех натуральных чисел от 100 до 3000?

def f(n):
    prev = n
    n = bin(n)[2:]
    s = ''
    flag = 0
    not_done = 1

    for i in n:
        if i == '1' and not not_done:
            not_done = 0
        else:
            not_done = 1
        if ((i == '1' and not flag) or (i == '0' and flag)) and not_done:
            flag = 1
            not_done = 0
        elif not not_done:
            s += i
            flag = 0
    s = s if s else '0'
    return prev - int(s, 2)


c = set()
for n in range(100, 3001):
    c.add(f(n))

print(len(c))
