a, b, d = map(int, input().split())
h_pot = abs(a - b) / 2 + a


# fixme не работает если |a-b|=1
def find_dist(check=False):
    tmp_right = h_pot if check else int(h_pot) + 1
    tmp_left = h_pot if check else int(h_pot)

    while (tmp_left % d) != 0:
        tmp_left -= 1
    while (tmp_right % d) != 0:
        tmp_right += 1
    dist = min(abs(tmp_left - h_pot), abs(tmp_right - h_pot))

    if check:
        return int(dist)

    if abs(tmp_left - h_pot) < abs(tmp_right - h_pot):
        h = int(h_pot)
    else:
        h = int(h_pot) + 1
    return h, dist


if h_pot.is_integer():
    dist_to_ice = find_dist(True)
    h = h_pot
else:
    h, dist_to_ice = find_dist()
print(*map(int, (h, dist_to_ice)))
