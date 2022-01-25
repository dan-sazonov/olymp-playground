ans = 0
def func (a, b):
    while (a != 0) and (b != 0):
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return(b)
    else:
        return(a)

for x in range(1, 51):
    for y in range(1, 51):
        print(func(x, y))