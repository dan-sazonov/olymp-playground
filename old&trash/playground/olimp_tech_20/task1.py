foo = []
with open('input.txt') as open_read:
	for line in open_read:
		foo.extend(line.strip().split())
	x = foo[0]
	n = foo[1]
	s = foo[2]
	w = foo[3]
	q = foo[4]
	m = foo[5]
	
print(x, n, s, w, q, m)