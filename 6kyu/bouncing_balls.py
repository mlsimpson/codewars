# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/solutions/python

def bouncing_balls(h, bounce, window):
    if (h <= 0) or (bounce <= 0) or (bounce >= 1) or (window >= h):
        return -1

    passes = 1
    h = h * bounce
    while h > window:
        h *= bounce
        passes += 2

    return passes

