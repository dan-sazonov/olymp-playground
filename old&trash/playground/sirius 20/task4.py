n = int(input())
pillars = [int(input()) for i in range(n)]
iter_counter = 0
limit = n + 1
pivot = 0

while iter_counter < n - 2:
    cycle_counter = 1
    iter_counter += 1
    pivot_old = pivot
    pivot = pillars[iter_counter]

    if pivot > pivot_old:
        while iter_counter < n - 1:
            iter_counter += 1
            cycle_counter += 1
            j = pillars[iter_counter]
            if j < pivot:
                if cycle_counter < limit:
                    pillar_start, pillar_end = iter_counter - cycle_counter + 1, iter_counter + 1
                    limit = cycle_counter
                break
            elif j == pivot:
                continue
            break
    continue

print(pillar_start, pillar_end if pillar_start and pillar_end else 0)

"""
3
9
8
5

3 6
"""
