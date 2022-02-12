# https://www.codewars.com/kata/555eded1ad94b00403000071/solutions/python

def series_sum(n):
    increase = 3
    base = 1
    output = 0

    while n > 0:
        output += (1/base)
        base += increase
        n -= 1

    return "{:.2f}".format(output)
