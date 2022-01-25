n = int(input())
tree = dict()

for _ in range(n - 1):
    child, parent = input().split()
    tree[child] = parent
    if parent not in tree.keys():
        tree[parent] = 0

for i, _ in sorted(tree.items()):
    counter = 0
    key = i
    while tree[key] != 0:
        if key in tree.keys():
            key = tree[key]
            counter += 1
        else:
            break
    print(i, counter)

