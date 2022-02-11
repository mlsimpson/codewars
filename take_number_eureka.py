# https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python
# ooh, a short version of dig_pow in the best practices solutions

def sum_dig_pow(a, b):
    res = []
    for i in range(a, b + 1):
        p = 1
        n_list = list(map(int, str(i)))
        tmp_sum = 0
        for num in n_list:
            tmp_sum += (num ** p)
            p += 1
        if i - tmp_sum == 0:
            res.append(i)
    return res

