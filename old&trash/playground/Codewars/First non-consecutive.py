def first_non_consecutive(arr):
    numbers = list(range(arr[0], len(arr) + arr[0]))
    for c in range(len(arr)):
        if numbers[c] != arr[c]:
            return arr[c]
    return None
