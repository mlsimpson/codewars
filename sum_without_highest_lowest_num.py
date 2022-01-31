def sum_array(arr):
    if not arr or len(arr) < 2:
        return 0

    arr = sorted(arr)

    return sum(arr[1:-1])
