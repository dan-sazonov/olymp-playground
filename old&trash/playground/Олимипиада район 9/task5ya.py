Fin = open('input.in')
foo = Fin.readline().split()

w = int(foo[0])

if ((w % 2) == 0) and w != 2:
     print('YES')
else:
    print('NO')
