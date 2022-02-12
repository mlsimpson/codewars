# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/solutions/python

def first_non_consecutive(arr):
    index = 1

    while index < len(arr):
        if arr[index] > (arr[index - 1] + 1):
            return arr[index]
        index += 1

