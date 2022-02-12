# https://www.codewars.com/kata/5503013e34137eeeaa001648/solutions/python

def diamond(n):
    if n < 1 or n % 2 == 0:
        return None

    mid = (n // 2)
    res = ''

    for i in range(n):
        spaces = abs(i - mid)
        chars = n - (spaces * 2)

        res += ' ' * spaces
        res += '*' * chars
        res += '\n'

    return res

