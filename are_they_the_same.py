# https://www.codewars.com/kata/550498447451fbbd7600041c/solutions/python

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False

    a1mul = [x*x for x in array1]

    return sorted(a1mul) == sorted(array2)

