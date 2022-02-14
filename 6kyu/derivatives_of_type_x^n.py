# https://www.codewars.com/kata/55e2de13b668981d3300003d/solutions/python
# bit nasty but w/e

def differentiate(poly):
    poly_split = poly.split('x')
    res = ''

    if len(poly_split) > 1:
        if poly_split[1]:
            poly_split[1] = poly_split[1].split('^')[1]

    if len(poly_split) > 1:
        if not poly_split[0]:
            poly_split[0] = 1

        if poly_split[0] == '-':
            poly_split[0] = '-1'

        if poly_split[1]:
            poly_split[0] = (int(poly_split[0]) * int(poly_split[1]))
            poly_split[1] = (int(poly_split[1]) - 1)
            if poly_split[1] == 1:
                res += str(poly_split[0]) + 'x'
            else:
                res += str(poly_split[0]) + 'x^' + str(poly_split[1])
        else:
            res += str(poly_split[0])
    else:
        res += '0'

    return res

