res = []
for _ in range(int(input())):
    player = []
    while len(player) < 5:
        player.append(int(input()))

    h, w, s, r, p = player
    high_than_range = (h > 220) + (w > 250) + (s > 20) + (r > 6) + (p > 7)
    upper_half = (h >= 205) + (w >= 225) + (s >= 15) + (r >= 4) + (p >= 5)
    in_range = (h in range(190, 221)) + (w in range(200, 251)) + (s in range(10, 21)) + (r in range(2, 7)) + (
            p in range(3, 8))

    if (high_than_range >= 3) and (h > 220 or w > 250):
        res.append('0')
    elif (high_than_range >= 2 and upper_half - high_than_range >= 1) or (in_range == 5 and upper_half >= 3):
        res.append('1')
    elif (high_than_range >= 1 and upper_half - high_than_range >= 1) or (upper_half >= 3):
        res.append('2')
    else:
        res.append('3')

print(*res, sep='\n')
