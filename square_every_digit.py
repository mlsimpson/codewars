# https://www.codewars.com/kata/546e2562b03326a88e000020/solutions/python

def square_digits(num):
    ints = [int(x) for x in str(num)]
    squares = [i*i for i in ints]
    squares_string = ''.join(str(i) for i in squares)
    return int(squares_string)

print(square_digits(9119))

