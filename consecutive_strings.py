# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/solutions/python

def longest_consec(strarr, k):
    if not strarr:
        return ""

    if k > len(strarr):
        return ""

    if k < 1:
        return ""

    max_string = ""
    max_length = 0

    for i in range(len(strarr) - k + 1):
        start_string = strarr[i]
        for j in range(1, k):
            start_string += strarr[i + j]
        # print(start_string)
        if len(start_string) > max_length:
            max_string = start_string
            max_length = len(start_string)

    return max_string

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
