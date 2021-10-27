s = int(input())
e = int(input())
n = int(input())
portals = [int(input()) for _ in range(n)]
cur_min_a = cur_min_b = 1000_000_000

for i in range(n):
    tmp_min_a = abs(portals[i] - s)
    if tmp_min_a < cur_min_a:
        cur_min_a = tmp_min_a

for j in range(n):
    tmp_min_b = abs(portals[j] - e)
    if tmp_min_b < cur_min_b:
        cur_min_b = tmp_min_b

if abs(s - e) <= cur_min_a + cur_min_b:
    print(abs(s - e))
else:
    print(cur_min_a + cur_min_b + 1)
