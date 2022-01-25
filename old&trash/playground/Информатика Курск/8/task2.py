# 99 баллов, на сотню - 111952 informatics
from itertools import count
n = int(input())
k = int(input())
ans = 0
total = 0

for i in count(k):
    total += i
    ans += 1
    if total >= n:
        break

print(ans if n != k else 1)
