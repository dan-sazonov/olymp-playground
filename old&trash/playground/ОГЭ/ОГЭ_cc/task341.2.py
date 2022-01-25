arr = []
while True:
    i = int(input())
    if i:
        arr.append(i)
    else:
        arr.sort()
        break
print(sum(arr[-2:]), sum(arr[:2]))
