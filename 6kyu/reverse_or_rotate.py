# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/solutions/python

def revrot(strng, sz):
    if not strng or sz < 1 or sz > len(strng):
        return ""

    res = ''


    for i in range(0, len(strng) - sz + 1, sz):
        curr_strng = strng[i:i + sz]
        sum_cubes = 0
        for num in curr_strng:
            sum_cubes += (int(num) ** 3)
        if sum_cubes % 2 == 0:
            res += reverse(curr_strng)
        else:
            res += rotate(curr_strng)

    return res

def rotate(s):
    return s[1:] + s[0]

def reverse(s):
    return s[::-1]

