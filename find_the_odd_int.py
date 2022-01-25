# https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/python

def find_it(seq):
    out = {}

    for num in seq:
        out.setdefault(num, 0)
        out[num] += 1

    for x in out:
        if out[x] % 2 != 0:
            return x

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
