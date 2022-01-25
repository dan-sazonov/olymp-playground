arr = [3, 5, 1, 5, 8, 9, 4, 10, 0, 13, 5]
i_max = arr[0]
j_max = arr[0]

for i in arr:
    if i > i_max:
        i_max = i
for j in arr:
    if i_max > j > j_max:
        j_max = j

print(i_max, j_max)
