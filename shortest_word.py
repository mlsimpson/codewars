# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python

def find_short(s):

    words = s.split()

    l = len(words[0])

    for word in words:
        if len(word) < l:
            l = len(word)

    return l

