# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/solutions/python

def accum(s):
    res = ''
    for i, char in enumerate(s.lower()):
        # print(char)
        new_i = i + 2
        for x in range(1, new_i):
            # print('x =', x)
            if x == 1:
                out = ''.join(char.upper())
            else:
                out += char
        # print(out)
        res += out + '-'

    print(res[:-1])

