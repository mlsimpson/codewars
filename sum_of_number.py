# https://www.codewars.com/kata/55f2b110f61eb01779000053/solutions/python

def get_sum(a,b):
    if a == b:
        return a

    sum = 0

    for i in range(min(a, b),  max(a, b) + 1):
        sum += i

    return sum

