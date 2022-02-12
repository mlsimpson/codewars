# https://www.codewars.com/kata/52c31f8e6605bcc646000082/solutions/python

def two_sum(numbers, target):
    numsdict = {}
    for i, n in enumerate(numbers):
        compliment = target - n
        if compliment in numsdict:
            return [numsdict[compliment], i]
        else:
            numsdict[numbers[i]] = i

