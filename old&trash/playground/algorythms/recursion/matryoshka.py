def foo(length):
    if length < 1:
        return 'Central element'
    else:
        print('Top' + str(length))
        print(foo(length - 1) if foo(length - 1) != None else '')
        print('Bottom' + str(length))

