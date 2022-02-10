# https://www.codewars.com/kata/566fc12495810954b1000030/solutions/python

def nb_dig(n, d):
    res = [0]

    while n > 0:
        res.append(n * n)
        n -= 1

    res = [str(i) for i in res]

    flat = []

    for i in res:
        for digit in list(i):
            flat.append(digit)

    return flat.count(str(d))

