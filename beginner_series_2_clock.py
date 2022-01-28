# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/solutions/python

def past(h, m, s):
    milliseconds = 1000

    seconds = milliseconds
    minutes = seconds * 60
    hours = minutes * 60

    return ((h * hours) + (m * minutes) + (s * seconds))
