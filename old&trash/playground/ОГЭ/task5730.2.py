foo = input().split()
ans = 0
for c in foo:
    c = int(c) #KISS
    if (c % 5 == 0) or (c % 9 == 0):
        ans += c
    else:
        continue
        
print(ans)
