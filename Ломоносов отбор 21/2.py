n = input()
k = 0
count = 0
ans = ''
while int(n) > 1:
    k = len(n)
    count += 1
    if k % 2 == 0:
        if n[:k // 2] < n[k // 2:]:
            n = n[:k // 2]
            ans += '3'
        elif int(n[k // 2:]) == 0:
            n = n[:k // 2]
            ans += '3'
        else:
            n = n[k // 2:]
            ans += '4'
    elif len(str((int(n) // 2))) % 2 == 0 and int(n) % 2 == 0 or n == '2':
        n = str((int(n) // 2))
        ans += '2'
    elif len(str((int(n) // 4))) % 2 == 0 and int(n) % 4 == 0 or n == '4':
        n = str((int(n) // 4))
        ans += '22'
    else:
        n = str(int(n) * 2)
        ans += '1'
print(count)
print(ans)