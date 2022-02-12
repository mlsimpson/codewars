# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/solutions/python

def wave(s):
    res = []

    for index, char in enumerate(s):
        if char == " ":
            continue
        res.append(s[:index] + s[index].upper() + s[index + 1:])

    return res
