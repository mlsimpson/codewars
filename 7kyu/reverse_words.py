# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/solutions/python

def reverse_words(text):

    outlist = []

    for s in text.split(' '):
        outlist.append(s[::-1])

    outstr = ' '.join(outlist)

    return outstr
