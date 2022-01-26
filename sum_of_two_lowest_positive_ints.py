# https://www.codewars.com/kata/558fc85d8fd1938afb000014/solutions/python

def sum_two_smallest_numbers(numbers):
    arr = [x for x in numbers if x > 0]

    arr = sorted(arr)

    return arr[0] + arr[1]

