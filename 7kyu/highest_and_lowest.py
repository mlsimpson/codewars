# https://www.codewars.com/kata/554b4ac871d6813a03000035/solutions/python

def high_and_low(numbers):

    num_list = [int(i) for i in numbers.split()]

    print(num_list)

    maxnum = num_list[0]
    minnum = num_list[0]

    for i in num_list:
        if i > maxnum:
            maxnum = i
        if i < minnum:
            minnum = i

    numbers = f"{maxnum} {minnum}"
    # print(numbers)
    # print(max(num_list), min(num_list))
    return numbers

high_and_low("1 2 3 4 5")
high_and_low("1 2 -3 4 5")

