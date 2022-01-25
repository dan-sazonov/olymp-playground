def capitalize(s):
    foo = []
    for u_case in range(0, len(s)):
        if u_case % 2 == 0:
            foo.append(s[u_case])
        else:
            foo.append(s[u_case].upper())
    return [''.join(foo).swapcase(), ''.join(foo)]
