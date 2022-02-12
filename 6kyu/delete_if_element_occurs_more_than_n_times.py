# https://www.codewars.com/kata/554ca54ffa7d91b236000023/solutions/python

def delete_nth(order,max_e):
    a1_count = {}
    res = []

    for i, x in enumerate(order):
        a1_count.setdefault(x, 0)
        a1_count[x] += 1
        if a1_count[x] <= max_e:
            res.append(x)

    return res
