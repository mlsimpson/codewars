# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/solutions/python

def race(v1, v2, g):
    if v1 > v2:
        return None

    total_seconds = (3600 * g) / (v2 - v1)

    secs = int(total_seconds % 60)
    mins = int((total_seconds / 60) % 60)
    hours = int(total_seconds / 3600)

    return [hours, mins, secs]

