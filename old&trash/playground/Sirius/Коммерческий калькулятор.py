from queue import PriorityQueue

input()
operands = PriorityQueue()
res = 0
for i in map(int, input().split()):
    operands.put(i)

while operands.qsize() > 1:
    s = operands.get() + operands.get()
    res += s * 0.05
    operands.put(s)

print(res)
