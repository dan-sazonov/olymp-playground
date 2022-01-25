import collections

q = collections.deque()

while True:
    ask = input().split()
    if ask[0] == 'exit':
        print('bye')
        break
    elif ask[0] == 'push_front':
        q.appendleft(ask[1])
        print('ok')
    elif ask[0] == 'push_back':
        q.append(ask[1])
        print('ok')
    elif ask[0] == 'size':
        print(len(q))
    elif ask[0] == 'clear':
        q = collections.deque()
        print('ok')
    elif q and ask[0] == 'pop_front':
        print(q.popleft())
    elif q and ask[0] == 'pop_back':
        print(q.pop())
    elif q and ask[0] == 'front':
        print(q[0])
    elif q and ask[0] == 'back':
        print(q[-1])
    else:
        print('error')
