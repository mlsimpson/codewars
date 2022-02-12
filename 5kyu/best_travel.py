# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/solutions/python
# I hate this, I wanna find a good solution w/out itertools

from itertools import combinations

def choose_best_sum(t, k, ls):
    combos = combinations(ls, k)
    maximum = 0

    for combo in combos:
        curr_sum = sum(combo)
        if curr_sum > maximum and curr_sum <= t:
            maximum = curr_sum

    return maximum if maximum > 0 else None

