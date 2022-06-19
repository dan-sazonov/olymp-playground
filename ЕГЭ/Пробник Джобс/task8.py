import itertools

arr = itertools.product('APRSU',  repeat=5)
c = 1

for i in arr:
    if i[0] == 'U':
        print(i, c)

    c += 1
