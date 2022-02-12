# https://www.codewars.com/kata/57f609022f4d534f05000024/solutions/python
# oh i hate this

def stray(arr):
    res = {}

    for i in arr:
        res.setdefault(i, 0)
        res[i] += 1

    for x in res:
        if res[x] == 1:
            return x

