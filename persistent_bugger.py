# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/solutions/python

def persistence(n):
    iterations = 0

    while (n // 10) != 0:
        n = multiply_digits(n)
        iterations +=1

    return iterations

def multiply_digits(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product

print(persistence(39))

