# https://www.codewars.com/kata/542c0f198e077084c0000c2e/solutions/python

# i hate this. totally naive
def divisors(n):
    res = [n]
    for i in range(1, n//2 + 1):
        if n % i == 0:
            res.append(i)
        i += 1

    print("n:", n, "res:", res)

    return len(res)

