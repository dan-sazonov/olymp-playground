print(sum(filter(lambda x: True if x % 8 == 0 and abs(x) < 100 else False, map(int, input().split()))))