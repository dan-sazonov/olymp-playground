# 114042
a = int(input())
b = int(input())
c = int(input())
counter = 0

while b > a:
    if (b - 2) < a or (b - 2) % c == 0:
        b -= 1
    else:
        b -= 2
    counter += 1

print(counter)