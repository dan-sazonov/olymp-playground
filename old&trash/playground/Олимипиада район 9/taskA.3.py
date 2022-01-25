w = int(input())
l = int(input())
h = int(input())

if w > l:
	a = l / h
	b = w / l
else:
	a = w / h
	b = l / w

if (a > 2) and (b < 2):
	print("good")
else:
	print("bad")
