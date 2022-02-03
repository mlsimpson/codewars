# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/solutions/python

import string

def high(x):
    max_word = ''
    max_score = 0

    a1 = list(string.ascii_lowercase)
    b1 = list(range(1, 27))

    alpha_word = dict(zip(a1, b1))

    x = x.split()

    for word in x:
        score = 0
        for char in word:
            score += alpha_word[char]
        if score > max_score:
            max_score = score
            max_word = word

    return max_word

