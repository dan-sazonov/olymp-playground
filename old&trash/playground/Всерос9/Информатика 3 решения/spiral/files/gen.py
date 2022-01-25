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

def printTest(n, d, k):
    global curTest
    print(curTest, ":", n)
    f = open("%02d" % curTest, "w")
    curTest += 1
    print(n, d, k, file=f)
    f.close()

# sample
printTest(13, 2, 2)

t = [
    [1, 1, 2],
    [2, 1, 2],
    [1000, 1, 2],

    [10, 2, 3],
    [100, 2, 3],
    [1000, 2, 3],

    [10, 1, 5],
    [100, 1, 5],
    [1000, 1, 5],

    [10, 3, 2],
    [100, 3, 2],
    [1000, 3, 2],

    [10, 3, 5],
    [100, 3, 5],
    [1000, 3, 5],

    [100, 10, 2],
    [1000, 10, 2],

    [100, 100, 2],
    [1000, 100, 2],

    [1000, 100, 4],
    [1000, 100, 5],

]

for n, d, k in t:
    printTest(n, d, k)