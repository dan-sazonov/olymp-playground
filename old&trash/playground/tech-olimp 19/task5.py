Fin = open('input.in').readline().split()
ict = int(Fin[0])
rus = int(Fin[1])
bio = int(Fin[2])
phs = int(Fin[3])
mat = int(Fin[4])
number = Fin[5]

if (ict >= 63) and (((rus >= 84) and (mat >= 78)) or ((rus >= 62) and (mat >= 86))):
    print(number, '|зачислен')
else:
    print(number, '|не зачислен')
