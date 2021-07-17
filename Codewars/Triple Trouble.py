def triple_trouble(one, two, three):
    bar = []
    for c in list(zip(one, two, three)):
        bar.append(''.join(c))
    return ''.join(bar)
