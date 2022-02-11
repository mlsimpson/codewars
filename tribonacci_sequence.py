# https://www.codewars.com/kata/556deca17c58da83c00002db/solutions/python
# signature.append(sum(signature[-3:])) also works!

def tribonacci(signature, n):
    three = signature[0]
    two = signature[1]
    one = signature[2]

    if n <= len(signature):
        return signature[:n]

    index = len(signature)
    while index < n:
        next_num = three + two + one
        signature.append(next_num)
        three = two
        two = one
        one = next_num
        index += 1

    return signature

