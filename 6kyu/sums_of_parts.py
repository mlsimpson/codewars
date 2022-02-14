# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/solutions/python

def parts_sums(ls):
    total_sum = sum(ls)
    out = [total_sum]

    for i in range(1, len(ls) + 1):
        total_sum -= ls[i - 1]
        out.append(total_sum)

    return out

