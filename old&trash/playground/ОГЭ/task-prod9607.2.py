foo = input().split()
ans = 0

for c in foo:
    c = int(c)
    if (c % 4 == 0) and (c % 7 != 0) and c != 7:
        ans += 1
    else:
        continue

print(ans)
