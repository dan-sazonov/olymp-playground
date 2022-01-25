import sys

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

def printTest(n, k, a):
    global curTest
    print(curTest, ":", n, k)
    f = open("%02d" % curTest, "w")
    curTest += 1
    print(n, k, file=f)
    print(*a, file=f)
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
            if isPrime(q) and q not in smallp:
                smallp.append(q)
                break
    return smallp

def genOkTest2(n, maxv, cnt, maxp):
    a = [1] * n
    pp = genSmallP(cnt, maxp)
    for i in range(n):
        while True:
            a[i] = 1
            for j in range(10):
                t = random.randint(0, len(pp) - 1)
                if a[i] * pp[t] <= maxv:
                    a[i] *= pp[t]
            if i == 0 or a[i] != a[i - 1]:
                break
    printTest(n, 2, a)

def genGoodTest(n, k, maxv, ans, cnt, maxp):
    a = [1] * n
    l = random.randint(0, n - k)
    r = l + k - 1
    pp = genSmallP(cnt, maxp)
    for i in range(n):
        while True:
            a[i] = 1
            if l <= i <= r:
                a[i] = ans
            for j in range(10):
                t = random.randint(0, len(pp) - 1)
                if a[i] * pp[t] <= maxv:
                    a[i] *= pp[t]
            if i == 0 or a[i] != a[i - 1]:
                break
    printTest(n, k, a)

def genGoodTestB(n, k, maxv, cnt, maxp):
    a = [1] * n
    l = random.randint(0, n - k)
    r = l + k - 1
    pp = genSmallP(cnt, maxp)
    ans = 1
    tt = random.randint(1, 5)
    for i in range(tt):
        ans = ans * pp[random.randint(0, len(pp) - 1)]
    for i in range(n):
        while True:
            a[i] = 1
            if l <= i <= r:
                a[i] = ans
            for j in range(10):
                t = random.randint(0, len(pp) - 1)
                if a[i] * pp[t] <= maxv:
                    a[i] *= pp[t]
            if i == 0 or a[i] != a[i - 1]:
                break
    printTest(n, k, a)

if len(sys.argv) == 1:
    # sample
    printTest(10, 4, [2, 3, 4, 8, 12, 6, 12, 18, 4, 3])

    # group 1
    printTest(2, 2, [12, 18])
    printTest(3, 2, [12, 18, 24])
    printTest(3, 2, [27, 18, 24])
    printTest(100, 2, [1] * 100)
    printTest(100, 2, [72] * 100)
    printTest(100, 2, [100] * 100)
    genOkTest2(100, 100, 3, 30)
    genOkTest2(100, 100, 4, 30)
    genOkTest2(100, 100, 5, 30)
    genOkTest2(100, 100, 8, 30)

    # group 2
    printTest(2, 2, [121212, 181818])
    printTest(3, 2, [121212, 181818, 242424])
    printTest(3, 2, [272727, 181818, 242424])
    printTest(100, 2, [720000] * 100)
    printTest(100, 2, [10**9] * 100)
    genOkTest2(100, 10**9, 3, 100)
    genOkTest2(100, 10**9, 4, 100)
    genOkTest2(100, 10**9, 5, 100)
    genOkTest2(100, 10**9, 8, 100)
    genOkTest2(100, 10**9, 10, 100)

    # group 3
    printTest(2, 2, [121212121212121212, 181818181818181818])
    printTest(3, 2, [121212121212121212, 181818181818181818, 242424242424242424])
    printTest(3, 2, [272727272727272727, 181818181818181818, 242424242424242424])
    printTest(100, 2, [10**18] * 100)
    genOkTest2(100, 10**18, 3, 100)
    genOkTest2(100, 10**18, 4, 100)
    genOkTest2(100, 10**18, 5, 100)
    genOkTest2(100, 10**18, 8, 100)
    genOkTest2(100, 10**18, 10, 200)
    genOkTest2(100, 10**18, 20, 500)

    # group 4
    genGoodTest(100,  3, 100, 12, 4, 30)
    genGoodTest(100, 10, 100, 15, 4, 30)
    genGoodTest(100, 20, 100, 2, 4, 30)
    genGoodTest(100, 50, 100, 6, 4, 30)
    genGoodTest(100, 90, 100, 20, 4, 30)
    genGoodTest(100,  3, 100, 14, 6, 30)
    genGoodTest(100, 10, 100, 21, 6, 30)
    genGoodTest(100, 20, 100, 10, 6, 30)
    genGoodTest(100, 50, 100, 19, 6, 30)
    genGoodTest(100, 90, 100, 30, 6, 30)

    # group 5

    genGoodTestB(100,  3, 10**18,  14, 300)
    genGoodTestB(100, 10, 10**18,  14, 300)
    genGoodTestB(100, 20, 10**18,  14, 300)
    genGoodTestB(100, 50, 10**18,  14, 300)
    genGoodTestB(100, 90, 10**18,  14, 300)
    genGoodTestB(100,  3, 10**18,  26, 300)
    genGoodTestB(100, 10, 10**18,  26, 300)
    genGoodTestB(100, 20, 10**18,  26, 300)
    genGoodTestB(100, 50, 10**18,  26, 300)
    genGoodTestB(100, 90, 10**18,  26, 300)

    exit(0)

curTest = int(sys.argv[1])
# group 6
if sys.argv[1] == "52": genGoodTest(500000,  3, 100, 12, 4, 30)
if sys.argv[1] == "53": genGoodTest(500000, 100, 100, 3, 4, 30)
if sys.argv[1] == "54": genGoodTest(500000, 2000, 100, 2, 4, 30)
if sys.argv[1] == "55": genGoodTest(500000, 10000, 100, 6, 4, 30)
if sys.argv[1] == "56": genGoodTest(500000, 20000, 100, 6, 4, 30)
if sys.argv[1] == "57": genGoodTest(500000, 30000, 100, 6, 4, 30)
if sys.argv[1] == "58": genGoodTest(500000, 50000, 100, 6, 4, 30)
if sys.argv[1] == "59": genGoodTest(500000, 70000, 100, 6, 4, 30)
if sys.argv[1] == "60": genGoodTest(500000, 100000, 100, 6, 4, 30)
if sys.argv[1] == "61": genGoodTest(500000, 400000, 100, 20, 4, 30)
           
# group 7
if sys.argv[1] == "62": genGoodTestB(500000,  3, 10**18, 6, 300)
if sys.argv[1] == "63": genGoodTestB(500000, 100, 10**18, 20, 300)
if sys.argv[1] == "64": genGoodTestB(500000, 2000, 10**18, 6, 300)
if sys.argv[1] == "65": genGoodTestB(500000, 10000, 10**18, 6, 300)
if sys.argv[1] == "66": genGoodTestB(500000, 20000, 10**18, 6, 300)
if sys.argv[1] == "67": genGoodTestB(500000, 30000, 10**18, 8, 300)
if sys.argv[1] == "68": genGoodTestB(500000, 50000, 10**18, 14, 300)
if sys.argv[1] == "69": genGoodTestB(500000, 70000, 10**18, 24, 300)
if sys.argv[1] == "70": genGoodTestB(500000, 100000, 10**18, 24, 300)
if sys.argv[1] == "71": genGoodTestB(500000, 400000, 10**18, 24, 300)

