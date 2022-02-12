# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/solutions/python
# single list comprehension suffices

def duplicate_encode(word):
    res_dict = {}
    word = word.lower()

    for char in word:
        res_dict.setdefault(char, 0)
        res_dict[char] += 1

    res = []
    for char in word:
        if res_dict[char] > 1:
            res.append(')')
        else:
            res.append('(')

    return ''.join(res)

