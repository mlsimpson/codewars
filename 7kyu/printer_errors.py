# https://www.codewars.com/kata/56541980fa08ab47a0000040/solutions/python

import string

def printer_error(s):

    alphabet_string = string.ascii_lowercase

    alphabet_string = alphabet_string[:13]

    # print(alphabet_string)

    s_length = len(s)

    s_error = 0

    for char in s:
        if char not in alphabet_string:
            s_error +=1

    return((str(s_error)) + "/" + (str(s_length)))

print(printer_error("abcdefghijklmnop"))
