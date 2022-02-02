# https://www.codewars.com/kata/56445c4755d0e45b8c00010a/solutions/python

def fortune(f0, p, c0, n, i):
    p = p * 0.01
    i = i * 0.01
    iterations = 1

    while iterations < n:
        f0 = int(f0 + (p * f0) - c0)
        if f0 < 0:
            return False

        c0 = int(c0 + (c0 * i))
        iterations += 1

    return True

