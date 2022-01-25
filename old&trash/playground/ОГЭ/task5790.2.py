foo = input().split()
amount = int(foo[0])
ans = 0
days = 0

for c in foo[1:]:
	c = int(c)
	if c > 0:
		ans += c
		days += 1
	else:
		continue
print(str(ans / days) + '\n' + str(days))