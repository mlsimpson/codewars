# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/solutions/python

def duplicate_count(text):
    text = text.lower()
    text_dict = {}
    res = 0
    for char in text:
        if char not in text_dict:
            text_dict[char] = 1
        else:
            text_dict[char] += 1
    for i in text_dict:
        if text_dict[i] > 1:
            res += 1
    return res

