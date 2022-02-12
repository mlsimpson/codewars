# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/solutions/python

def max_sequence(arr):
    if not arr:
        return 0

    curr_sum = arr[0]
    max_sum = curr_sum

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum if max_sum > 0 else 0

# or

def max_sequence2(arr):

    curr_sum, max_sum = 0, 0

    for num in arr:
        curr_sum += num
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

