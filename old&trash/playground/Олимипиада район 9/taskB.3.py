n = open('input.in').readline().split()
n = int(n[0])
sq = 0

for c in range(1, n):
	if (c * c) <= n:
		sq += 1
		n -= (c * c)
	else:
		break
print(sq)