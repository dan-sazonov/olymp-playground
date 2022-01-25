with open('input.txt') as input_file:
    pieces = list(input_file.read().split('\n'))

f, s, res = [], [], []

for object_ in pieces:
    if object_.startswith('0') or object_.endswith('0'):
        s.append(object_)
    else:
        f.append(object_)

list(map(int, f)).sort()
f.reverse()
res.extend(f)
while s:
    elem = min(s, key=lambda x: x.count('0'))
    print(elem)
    s.remove(elem)
    res.append(elem)

print(''.join(res))
#