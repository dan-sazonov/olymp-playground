n = int(input())
codes = dict()
for _ in range(n):
    code, name = input().split()
    if name in codes.keys():
        codes[name].append(code)
    else:
        codes[name] = [code]

m = int(input())
for _ in range(m):
    name = input()
    if name in codes.keys():
        print(*codes[name])
    else:
        print('NOT')
