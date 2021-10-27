x = int(input())
y = int(input())
n = int(input())
a = x + y

if n % a:
    if (n % a) > y:
        print(((n // a) * 2) + 2)
    else:
        print(((n // a) * 2) + 1)
else:
    print((n / a) * 2)