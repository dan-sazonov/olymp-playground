class Random:
    seed = 0

    def __init__(self):
        pass

    def randint(self, l, r):
        self.seed = self.seed * 5 % (10**18 + 3)
        return self.seed % (r - l + 1) + l

random = Random()

random.seed = 8979123719

curTest = 1

def printTest(n, t):
    global curTest
    print(curTest, ":", n, t)
    f = open("%02d" % curTest, "w")
    curTest += 1
    print(n, t, file=f)
    f.close()

maxn = 10
zero = [0] * (maxn + 1)
zero[2] = 1
for i in range(3, maxn + 1):
    zero[i] = (zero[i - 1] + zero[i - 2]) * (i - 1)
print(zero)
# sample
printTest(3, 1)

# group 1
x = [
    2, 4, 6, 8, 10
]
for n in x:
    printTest(n, 1)

# group 2
x = [
    20, 42, 100, 666, 1000
]
for n in x:
    printTest(n, 1)

# group 3
x = [
    5, 7, 9
]
for n in x:
    printTest(n, 1)

# group 4
x = [
    11, 41, 73, 111, 555, 777, 999
]
for n in x:
    printTest(n, 1)

# group 5
x = [3, 4, 5, 6, 7]
for n in x:
    printTest(n, zero[n])

# group 6
x = [4, 5, 6, 7, 8, 9, 10, 10, 10]
for n in x:
    printTest(n, random.randint(1, min(10000, zero[n])))
printTest(10, 10000)

# group 7
printTest(100, 1000)
printTest(1000, 100)
for i in range(8):
    n, t = random.randint(11, 1000), random.randint(1, 10000)
    while n * t > 100000:
        n, t = random.randint(11, 1000), random.randint(1, 10000)
    printTest(n, t)