def longest_consec(strarr, k):
    i = 0
    j = k
    ans = ''

    if k < 1:
        return ''

    while j <= len(strarr):
        tmp = ''.join(strarr[i:j])
        if len(ans) < len(tmp):
            ans = tmp
        i += 1
        j += 1

    return ans

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
