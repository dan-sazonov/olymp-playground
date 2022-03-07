for x in 0, 1:
    for i in 0, 1:
        for j in 0, 1:
            print(f'{x=} {i=} {j=} | {((not (i or x)) or j or x)}, {(j or x)}')
            if ((not (i or x)) or j or x) != (j or x):
                # print(f'fuckup: {x=} {i=} {j=}')
                pass
