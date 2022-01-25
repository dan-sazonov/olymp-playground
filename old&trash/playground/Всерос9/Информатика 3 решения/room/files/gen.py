class Random:
    seed = 0

    def __init__(self):
        pass

    def randint(self, l, r):
        self.seed = self.seed * 5 % 1000000007
        return self.seed % (r - l + 1) + l

random = Random()

random.seed = 8979123719

curTest = 1

def printTest(w, l, h):
    global curTest
    print(curTest, ":", w, l, h)
    f = open("%02d" % curTest, "w")
    curTest += 1
    print(w, file=f)
    print(l, file=f)
    print(h, file=f)
    f.close()

def randomTest(n, k, maxv):
    a = []
    for i in range(n):
        a.append(random.randint(1, maxv))
    printTest(n, k, a)

def isPrime(p):
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True

def genSmallP(cnt, maxv):
    smallp = []
    for i in range(cnt):
        while True:
            q = random.randint(1, maxv)
            if isPrime(q):
                smallp.append(q)
                break
    return smallp

def genGoodTest(n, k, maxv, ans, cnt, maxp):
    a = [1] * n
    l = random.randint(0, n - k)
    r = l + k - 1
    pp = genSmallP(cnt, maxp)
    for i in range(n):
        if l <= i <= r:
            a[i] = ans
        for j in range(10):
            t = random.randint(0, len(pp) - 1)
            if a[i] * pp[t] <= maxv:
                a[i] *= pp[t]
    printTest(n, k, a)

# sample
printTest(4000, 6000, 3000)
printTest(4600, 8600, 1600)

#
t = [
    [1000, 1000, 1000],
    [1000, 10000, 1000],
    [10000, 1000, 1000],
    [1000, 1000, 10000],
    [10000, 10000, 1000],

    [10000, 10000, 10000],
    [4000, 3000, 1000],
    [4000, 8000, 2000],
    [3333, 6666, 1111],
    [7777, 5555, 2222],
]
for w, l, h in t:
    printTest(w, l, h)