ans = []

for i in range(1000, 10_000):
    if len(set(str(i))) == 4:
        ans.append(i)

print(len(ans))
