import random


def counter(matrix):
    for x in matrix:
        for y in range(0, len(x)):
            x[y]


def rand_matrix(n=int(input()), m=int(input())):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for c in range(0, m):
            matrix[i].append(random.randint(0, 1))

    # return counter(matrix)
    return matrix


print(rand_matrix())
# TODO переделать!