foo = input().split()
ans = 0

for c in foo:
    c = int(c)
    if c == 0:
        break
    elif str(c)[-1] == '0' and c % 7 == 0:
        ans += c
    else:
        continue
        #14 140 20 70

print(ans)