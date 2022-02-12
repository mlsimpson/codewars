# https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions/python

def to_jaden_case(string):
    words = string.split()
    res = ''
    for word in words:
        # print(word[0].upper() + word[1:])
        res += word[0].upper() + word[1:] + " "
    return str(res[:-1])

# return " ".join(w.capitalize() for w in s.split())

