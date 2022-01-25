current, need = input().split()
rows = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x_move = abs(int(current[1]) - int(need[1]))
y_move = abs(int(rows[current[0]]) - int(rows[need[0]]))
if current[0] >= need[0] or x_move > y_move:
    print('NO')
    exit()
current_sum = int(rows[current[0]]) + int(current[1])
need_sum = int(rows[need[0]]) + int(need[1])
if max(need_sum, current_sum) % min(need_sum, current_sum) == 0:
    print('YES')
else:
    print('NO')
