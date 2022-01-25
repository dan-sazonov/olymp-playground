# 40 баллов, сотня - 111954
n = int(input())
nums = [int(input()) for _ in range(n)]
ans = [0] * n
nums.sort(key=lambda x: nums.count(x))
seq = [0] * n
last_ins = (n - 1) // 2

for i in range(n):
    ins = None
    if i % 2 == 0:
        ins = i // 2
        if ins < 0:
            ins = i
    seq[i] = ins
for j in range(1, n, 2):
    last_ins += 1
    seq[j] = last_ins

for k in range(n):
    ans[k] = nums[seq[k]]
    if k > 0 and ans[k] == ans[k - 1]:
        print(0)
        break
else:
    print(*ans)
