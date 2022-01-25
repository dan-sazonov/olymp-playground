from itertools import product

n = int(input())

counter = 0
for i in product(*['abc'] * n):
    for j in range(1, len(i)):
        if i[j - 1] == i[j] == 'a':
            continue
        counter += 1

print(counter)
