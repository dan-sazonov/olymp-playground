from collections import deque

st1 = deque(map(int, input().split()))
st2 = deque(map(int, input().split()))
counter = 0

while st1 and st2 and counter <= 10e6:
    print(st1, st2)
    if st1[0] == 0:
        st1[0] = 10
    if st2[0] == 0:
        st2[0] = 10
    if st1[0] > st2[0]:
        st1.append(st2[0])
        st2.popleft()
    elif st1[0] < st2[0]:
        st2.append(st1[0])
        st1.popleft()
    counter += 1

print(st1, st2, counter)
