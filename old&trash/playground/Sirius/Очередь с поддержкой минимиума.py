import collections

q = collections.deque()
log = []

for _ in range(int(input())):
    i = int(input())
    if i:
        q.append(i)
    elif q and not i:
        log.append(min(q))
        q.popleft()
    else:
        log.append(-1)

print(*log, sep='\n')
