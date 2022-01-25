from itertools import combinations_with_replacement, permutations

with open('input.txt') as open_read:
    n = int(open_read.read())

stacks = list(combinations_with_replacement(['a', 'b', 'c'], 3))
out = len(stacks)
print(stacks)
for stack in stacks:
    print(stack, out)
    if stack[0] == stack[1] == 'a':
        out -= 1
print(out)
