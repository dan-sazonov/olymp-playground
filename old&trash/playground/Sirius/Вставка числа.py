n = int(input())
a = list(map(int, input().split()))
number, index = map(int, input().split())

a.insert(index - 1, number)
print(*a)
