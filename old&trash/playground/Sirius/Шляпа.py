words = dict()
n, m = map(int, input().split())
ans = [0] * n
for _ in range(m):
    team, word = input().split()
    words[word] = int(team) - 1

for i in words:
    ans[words[i]] += 1

print(*ans)
