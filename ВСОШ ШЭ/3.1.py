s = int(input())
e = int(input())
n = int(input())
portals = []
a = b=  1000000000
for i in range(0, n):
    x = int(input())
    portals.append(x)

for i in range(0, n):
    if (abs(portals[i] - s)) < a:
        a = abs(portals[i] - s)

for i in range(0, n):
    if (abs(portals[i] - e)) < b:
        b = abs(portals[i] - e)

if abs(s - e) < (a + b + 1):
    print(abs(s - e))
else:
    print(a + b + 1)
