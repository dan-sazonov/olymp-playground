n = int(input())

def funk(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return funk(n - 1) +  funk(n - 2)

print(funk(n))