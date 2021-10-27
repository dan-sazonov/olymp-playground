x = int(input())
y = int(input())
n = int(input())
a = x + y

if not (n % a):
    b = int(n/a)
    b = b * 2
    print(int((n / a) * 2))
else:
    if (n % a) > y:
        c = int(n // a)
        c = c * 2 + 2
        print(((n // a) * 2) + 2)
    else:
        c = int(n // a)
        c = c * 2 + 1
        print(((n // a) * 2) + 1)
