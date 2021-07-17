def digital_root(n):
    return n if n < 10 else digital_root(sum(list(map(int, str(n)))))
