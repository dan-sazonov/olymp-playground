# fixme не сработает при нескольких парах с равной суммой
n, k = map(int, input().split())
pairs = dict()
i = j = 1
col1 = []
col2 = []

while i <= n:
    ft, sd = map(int, input().split())
    if ft + sd in pairs.keys():
        pairs[ft + sd].append({i, i + 1})
    else:
        pairs[ft + sd] = [{i, i + 1}]
    col1.append(ft)
    col2.append(sd)
    i += 1

j = 1
for i in range(n - 1):
    tmp = col1[i] + col1[i + 1]
    if tmp in pairs.keys():
        pairs[tmp].append({j, j + 2})
    else:
        pairs[tmp] = [{j, j + 2}]

    tmp = col2[i] + col2[i + 1]
    if tmp in pairs.keys():
        pairs[tmp].append({j + 1, j + 3})
    else:
        pairs[tmp] = [{j + 1, j + 3}]
    j += 2
print(pairs)
'''
4 2
1 2
3 4
5 6
7 8
'''
'''
3 2
2 2
3 3
2 1
'''