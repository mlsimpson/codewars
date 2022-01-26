# https://www.codewars.com/kata/54ff3102c1bad923760001f3/solutions/python

def get_count(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')

    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count
