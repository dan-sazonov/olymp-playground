def move_zeros(array):
    counter = 0
    ans = []
    for i in array:
        if i == 0 and (type(i) == int or type(i) == float):
            counter += 1
        else:
            ans.append(i)
    ans.extend([0] * counter)
    return ans
