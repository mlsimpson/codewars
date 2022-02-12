# https://www.codewars.com/kata/530e15517bc88ac656000716/solutions/python

import string

def rot13(message):
    alpha_list = string.ascii_lowercase

    res = ''

    for char in message:
        if not char.isalpha():
            res += char
        else:
            if char.islower():
                res += alpha_list[(alpha_list.index(char) + 13) % 26]
            else:
                res += alpha_list[(alpha_list.index(char.lower()) + 13) % 26].upper()

    return res

