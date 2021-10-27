x = int(input())
y = int(input())
n = int(input())
a = x + y

if (n % a) == 0:
    print(n * 2 // a)
else:
    if (n % a) <= y:
        print((n * 2 // a) + 1)
    else:
        print((n * 2 // a) + 2)