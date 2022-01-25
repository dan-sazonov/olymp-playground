foo = input().split()
amount = int(foo[0])
done = 0
ans = 0

for c in foo[1:]:
	c = int(c)
	if c >= 8:
		done += 1
		ans += c
	else:
		continue

print(done, '\n' + str(ans / done))