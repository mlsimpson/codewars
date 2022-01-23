# https://www.codewars.com/kata/546f922b54af40e1e90001da/solutions/python

import string

def alphabet_position(text):

    alphadict = dict(zip(string.ascii_lowercase, range(1, 27)))

    text = [char.lower() for char in text if char.isalpha()]

    number_representation = []
    for char in text:
        number_representation.append(str(alphadict[char]))

    return " ".join(number_representation)



print(alphabet_position("The narhwal bacons at midnight."))

