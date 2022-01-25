foo = input().split()
foo = [int(item) for item in foo]
foo.sort()
print(str(foo[0] + foo[1]), str(foo[-1] + foo[-2]))