n = int(input())
tmp = input().split()
state = []

for i in range(n):
    state.append([int(tmp[i]), i + 1])

for _ in range(int(input())):
    x = int(input())
    for j in range(n):
        if state[j][1] == x - 1:
            state[j][1] += 1
        elif state[j][1] == x:
            state[j][1] -= 1

print(*map(lambda x: x[0], sorted(state, key=lambda x: x[1])))
