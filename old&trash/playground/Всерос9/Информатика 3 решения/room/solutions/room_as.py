w = int(input())
l = int(input())
h = int(input())

if w < l:
    w, l = l, w

if l >= 2 * h and w <= 2 * l:
    print("good")
else:
    print("bad")
