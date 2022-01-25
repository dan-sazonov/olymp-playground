foo = input().split()
ans = 0
for c in foo:
    if (int(c) % 4 == 0) and (c[-1] == '6'):
        ans += int(c)
    else:
        continue
print(ans)