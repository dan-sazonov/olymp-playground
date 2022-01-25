string = input()
x = 0
y = 0
directions = ['w', 'a', 's', 'd']
pointer = 0
counter = 0
was_here = {(0, 0)}

for i in string:
    if i == 'L':
        pointer += 1
    if i == 'R':
        pointer -= 1
    orient = directions[pointer]
    if i == 'S':
        if orient == 'w':
            y += 1
        elif orient == 's':
            y -= 1
        elif orient == 'a':
            x -= 1
        elif orient == 'd':
            x += 1
        counter += 1
        if (x, y) in was_here:
            print(counter)
            break
        was_here.add((x, y))
else:
    print(-1)
