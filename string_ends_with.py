# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/solutions/python
# also string.endswith(ending)

def solution(string, ending):
    if not ending:
        return True

    endlen = 0 - len(ending)

    return string[endlen:] == ending
