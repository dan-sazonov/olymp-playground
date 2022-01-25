area_min, area_max, perim_min, perim_max = map(int, input().split())
counter = 0

for a in range(1, min(area_max // area_min, int(area_max ** .5) + 20)):
    for b in range(1, perim_max + 1):
        if area_min <= a * b <= area_max and perim_min <= (a + b) * 2 <= perim_max and a <= b:
            # if (b, a) not in ans:
            #     # print(a, b)
            counter += 1
print(counter)
