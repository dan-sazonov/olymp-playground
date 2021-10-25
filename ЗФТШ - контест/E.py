max_1, max_2 = 0, 0

with open('input.txt', 'r') as in_file:
    file = in_file.read().split('\n')
    for i in map(int, file[1].split()):
        if i > max_1:
            max_1 = i
        if max_1 > i > max_2:
            max_2 = i
#
# max_1, max_2 = 0, 0
#
# for i in x:
#     if i > max_1:
#         max_1 = i
#     if max_1 > i > max_2:
#         max_2 = i

with open('output.txt', 'w') as out_file:
    out_file.write(str(max_1 * max_2))
