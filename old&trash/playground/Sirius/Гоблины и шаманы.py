# from collections import deque
#
# n = int(input())
# first = deque(maxlen=n)
# second = deque(maxlen=n)
# ans = []
#
# for i in range(n):
#     ask = input().split()
#     if ask[0] == '-':
#         ans.append(first.popleft())
#     elif ask[0] == '+':
#         second.append(ask[1])
#     else:
#         second.appendleft(ask[1])
#     if len(second) >= len(first):
#         x = second.popleft()
#         first.append(x)
#
# print(*ans, sep='\n')

# from collections import deque
#
# n = int(input())
# first = deque(maxlen=n)
# second = deque(maxlen=n)
# ans = []
#
# for i in range(n):
#     ask = input().split()
#     if ask[0] == '-':
#         ans.append(first.popleft())
#     elif ask[0] == '+':
#         second.append(ask[1])
#     else:
#         second.appendleft(ask[1])
#     if len(second) > len(first):
#         x = second.popleft()
#         first.append(x)
#
# print(*ans, sep='\n')
