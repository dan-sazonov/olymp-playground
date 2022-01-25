import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

a = dict(sorted(d.items(), key=lambda x: x[1]))
b = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
x = dict(sorted(d.items(), key=operator.itemgetter(1)))
y = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print(a, b, x, y, sep='\n')