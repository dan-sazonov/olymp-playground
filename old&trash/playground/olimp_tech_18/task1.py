from itertools import permutations

perm = permutations(['X', '7', '7', '2', 'K', 'X'])
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
out = []
for i in list(perm):
    if i[1] in numbers and i[2] in numbers and i[3] in numbers:
        out.append(''.join(i))
out = set(out)
print(len(out))
for elem in out:
    print(elem)
