for i in range(125256, 125331, 2):
    ans = []
    for j in range(2, i+1, 2):
        if i % j == 0:
            ans.append(j)
        if len(ans) > 6:
            break
    else:
        if len(ans) == 6:
            print(*ans)
