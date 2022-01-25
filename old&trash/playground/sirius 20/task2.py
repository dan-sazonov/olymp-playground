a = int(input()) - 1
b = int(input()) - 1
c = int(input()) - 1
time = 0

while min(a, b, c) > 0:
    time += 1
    if time % 2 == 1:
        b -= 1
    elif time % 4 == 2:
        a -= 1
    elif time % 4 == 3:
        c -= 1

if not a or not c:
    print(time + 6)
elif not b:
    print(time + 4)
else:
    print(time)
