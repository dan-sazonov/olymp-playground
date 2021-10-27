x = int(input())
y = int(input())
n = int(input())
sum = (x + y)
if not (n % (x + y)):
    print(int((n / sum) * 2))
else:
    if (n % (x + y)) > y:
        print(int(((n // sum) * 2) + 2))
    else:
        print(int(((n // sum) * 2) + 1))
