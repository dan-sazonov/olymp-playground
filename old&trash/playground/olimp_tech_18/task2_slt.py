with open('input.txt') as input_file:
    pieces = list(input_file.read().split('\n'))

f, s, res = [], [], []

for object_ in pieces:
    # Делим куски на те, в которых нет нулей и на те, в которых есть нули
    if object_.startswith('0') or object_.endswith('0'):
        s.append(object_)
    else:
        f.append(object_)

while f:
    elem = max(f)
    f.remove(elem)
    res.append(elem)

while s:
    elem = min(s, key=lambda x: x.count('0'))
    print(elem)
    s.remove(elem)
    res.append(elem)

print(''.join(res))
