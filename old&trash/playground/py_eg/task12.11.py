import random


def rand_matrix(n=int(input())):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for c in range(0, n):
            matrix[i].append(random.randint(0, 1))

    return matrix


print(rand_matrix())
