def solve(n):
    from math import sqrt
    '''
    int N = -1;
    for (int a = Math.Ceiling(Math.Sqrt(n)) - 1; a > 0; a--) {
       if (n % a == 0) {
          int bma = n / a - a;
          if (bma % 2 == 0) {
             int p = bma / 2;
             int N = p * p;
             break;
          }
       }
    }
    '''
    res = -1
    a = int(sqrt(n))
    while a > 0:
        if n % a == 0:
            bma = n / a - a
            if bma % 2 == 0:
                p = bma / 2
                res = p * p
                break
        a -= 1
    return res, p, a, bma

print(solve(int(input())))
