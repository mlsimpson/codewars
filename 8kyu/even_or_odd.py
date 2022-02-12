# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/solutions/python

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))
print(even_or_odd(1))
print(even_or_odd(11))
print(even_or_odd(12))

