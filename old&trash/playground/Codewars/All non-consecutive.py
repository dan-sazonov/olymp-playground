def all_non_consecutive(arr):
    a = 0
    out = []
    for i in enumerate(arr):
        i = list(i)
        i[0] += a
        if i[0] + 1 != i[1]:
            a += i[1] - i[0]
            print(i[1])


all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10])
# Test.assert_equals(all_non_consecutive([1,2,3,4,6,7,8,10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
