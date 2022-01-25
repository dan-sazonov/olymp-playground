from bisect import *

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in b:
    L = bisect_left(a, i)
    R = bisect_right(a, i)
    print(R - L)
