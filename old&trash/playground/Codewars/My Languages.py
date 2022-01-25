def my_languages(results):
    foo = list(results.items())
    foo.sort(key=lambda x: x[1])
    foo.reverse()
    return [i[0] for i in foo if i[1] >= 60]
