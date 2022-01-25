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

def printTest(n):
    global curTest
    print(curTest, ":", n)
    f = open("%02d" % curTest, "w")
    curTest += 1
    print(n, file=f)
    f.close()

# sample
printTest(10)

# group 1
t = [
    1, 4, 5, 33, 100, 
    sum([i * i for i in range(1, 10)]), 
    sum([i * i for i in range(1, 10)]) - 1, 
    sum([i * i for i in range(1, 10)]) + 1, 
    sum([i * i for i in range(1, 14)]), 
    1000
]
for n in t:
    printTest(n)

# group 2

t = [
    sum([i * i for i in range(1, 1000)]), 
    sum([i * i for i in range(1, 1000)]) - 1, 
    sum([i * i for i in range(1, 1000)]) + 1, 
    sum([i * i for i in range(1, 1442)]), 
    1000000000,
    random.randint(1, 10**9),
    random.randint(1, 10**9),
    random.randint(1, 10**9),
    random.randint(1, 10**9),
    random.randint(1, 10**9)
]
for n in t:
    printTest(n)

# group 3

t = []
s = 0
i = 1
while s + i * i < 10**12:
    s += i * i
    i += 1
t.append(s)
t.append(s + 1)
t.append(s - 1)
t.append(10 ** 12)
t.append(10 ** 12 - 1)
for i in range(5):
    t.append(random.randint(1, 10**12))

for n in t:
    printTest(n)


# group 4

t = []
s = 0
i = 1
while s + i * i < 10**18:
    s += i * i
    i += 1
t.append(s)
t.append(s + 1)
t.append(s - 1)
t.append(10 ** 18)
t.append(10 ** 18 - 1)
for i in range(5):
    t.append(random.randint(1, 10**18))

for n in t:
    printTest(n)
