# https://www.codewars.com/kata/5842df8ccbd22792a4000245/solutions/python
# clever:
# num = list(str(num))
# return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

def expanded_form(n):
    out = []
    out2 = []

    while n > 0:
        out.append(n % 10)
        n //= 10

    out.reverse()

    for i, num in enumerate(out):
        if num != 0:
            out2.append(str(num * (10 ** (abs(i - (len(out) - 1))))))

    return ' + '.join(out2)

