n = input()
s = {item: 0 for item in range(10)}
for i in n:
    if i.isdigit():
        s[int(i)] += 1
res = ''
resc = ('' if s[0] % 2 == 0 else '0')
for j in range(1, 10):
    res += str(j) * (s[j] // 2)
res0 = '0' * (s[0] // 2)
for i in range(10):
    if s[i] % 2 == 1:
        resc = str(i)
        break
if len(res) > 0:
    res = res[0] + res0 + (res[1:] if len(res) > 1 else '')
    res = res + resc + res[::-1]
else:
    res = (resc if s[0] == 0 else '0')
print(res)
