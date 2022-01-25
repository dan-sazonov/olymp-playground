n = input()
s = {item: 0 for item in range(10)}
res = ''
for i in n:
    if i.isdigit():
        s[int(i)] += 1
tmp = ('' if s[0] % 2 == 0 else '0')
res_0 = '0' * (s[0] // 2)

for i in range(1, 10):
    res += str(i) * (s[i] // 2)

for j in range(10):
    if s[j] % 2 == 1:
        tmp = str(j)
        break

if len(res):
    res_tmp = res[0] + res_0 + (res[1:] if len(res) > 1 else '')
    res = res_tmp + tmp + res_tmp[::-1]
else:
    res = (tmp if s[0] == 0 else '0')

print(res)
