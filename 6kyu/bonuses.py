# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6/solutions/python
# oof. inverse variation over three variables
# arr[0]*x == arr[1]*y, and so on...

def bonus(arr, s):
    coefficients = []
    out = []

    for i in arr:
        coefficients.append(i)

    x = arr[0]
    for i in range(len(coefficients)):
        coefficients[i] = x / coefficients[i]

    multiplier = sum(coefficients)
    target = (s / multiplier) * arr[0]

    for i in arr:
        out.append(round(target / i))

    return out


