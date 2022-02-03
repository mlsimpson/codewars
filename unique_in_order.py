# https://www.codewars.com/kata/54e6533c92449cc251001667/solutions/python

def unique_in_order(iterable):
    if not iterable:
        return []

    res = [iterable[0]]

    index = 0

    for char in iterable:
        if res[index] != char:
            res.append(char)
            index += 1

    return res

