n = int(input())
ans = {39: 987654, 33: 876543, 27: 765432, 21: 654321, 15: 543210}

if n in ans.keys():
    print(ans[n])
else:
    print('impossible')
