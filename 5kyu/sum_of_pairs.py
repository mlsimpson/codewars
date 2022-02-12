# https://www.codewars.com/kata/54d81488b981293527000c8f/solutions/python

def sum_pairs(ints, s):
    diff_dict = {}

    for num in ints:
        if (s - num) in diff_dict:
            return([s - num, num])

        diff_dict[num] = (s - num)

