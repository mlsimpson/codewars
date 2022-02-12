# https://www.codewars.com/kata/55685cd7ad70877c23000102/solutions/python

def make_negative(number):
    if number == 0:
        return 0
    if number > 0:
        return (0 - number)
    if number < 0:
        return number

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))
