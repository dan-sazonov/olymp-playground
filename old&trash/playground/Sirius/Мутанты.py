import bisect

n = int(input())
colors = list(map(int, input().split()))
m = int(input())
ask = list(map(int, input().split()))

for i in ask:
    print(bisect.bisect_right(colors, i) - bisect.bisect_left(colors, i))
