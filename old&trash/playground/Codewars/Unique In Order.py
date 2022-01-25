def unique_in_order(iterable):
    last = ''
    res = []
    for i in range(len(iterable)):
        if iterable[i] != last:
            res.append(iterable[i])
        last = iterable[i]
    return res
