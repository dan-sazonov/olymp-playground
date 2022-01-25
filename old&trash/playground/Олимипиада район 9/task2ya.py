Fin = open("input.in")
foo = Fin.readline().split()

d = int(foo[0])
a = int(foo[1])
b = int(foo[2])
s = int(foo[3])
t = int(foo[4])

if abs(a - b) > 180:
    m = (360 - abs(a - b))
else:
    m = abs(a - b)
if (m % t) > 0:
    turn = m // t + 1
else:
    turn = m // t

steps = turn + (d // s)
if (d % s) > 0:
    steps += 1

print(steps)
