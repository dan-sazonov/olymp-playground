input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))

ans = a ^ b
print(len(ans))
print(*sorted(ans))
