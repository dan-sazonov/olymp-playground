foo = input().split()
ans = 0
for c in foo:
	c = int(c)
	if (abs(c) < 100) and (c % 8 == 0) and c != 8:
		ans += c
	else:
		continue
print(ans)