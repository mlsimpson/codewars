# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/solutions/python
# a, b = set(arr)
# return a if arr.count(a) == 1 else b

def find_uniq(arr):
    num_dict = {}

    for num in arr:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1

    for key in num_dict:
        if num_dict[key] == 1:
            return key

