def foo(n):
    n = bin(n)[2:]
    return int(n + n[0:2][::-1], 2)


i = 0

while True:
    n = foo(i)
    if n > 90:
        print(i)
        break
    i += 1
