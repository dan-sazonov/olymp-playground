import bisect

n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))
shirts_min = pants_min = 0
diff_min = 10e7


for i in shirts:
    tmp = pants[bisect.bisect_right(pants, i) - 1]
    if i - tmp < diff_min:
        diff_min = i - tmp
        shirts_min = i
        pants_min = tmp

print(shirts_min, pants_min)
