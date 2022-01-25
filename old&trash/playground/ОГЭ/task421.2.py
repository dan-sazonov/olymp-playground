foo = input().split()
low_speed = 0
speed = 0

for c in range(1, int(foo[0]) + 1):

    if int(foo[c]) <= 40:
        low_speed += 1

    speed += int(foo[c])

print(round(speed / int(foo[0]), 1), 'no' if low_speed > 2 or low_speed == 0 else 'yes')