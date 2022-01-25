with open('input.in') as Fin:
    foo = Fin.readlines()
m = int(foo[0])
x = int(foo[1])
y = int(foo[2])
w = int(foo[3])
h = int(foo[4])

if (y % m) > 0:
    ansW = w // m + 1
else:
    ansW = w // m
if (x % m) > 0:
    ansH = h // m + 1
else:
    ansH = h // m
print(ansW * ansH)