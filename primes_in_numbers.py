#

def prime_factors(n):
    i = 2
    factors = {}

    while (i * i) <= n:
        if (n % i) == 0:
            factors.setdefault(i, 0)
            factors[i] += 1
            n //= i
        else:
            i += 1

    if n > 1:
        factors.setdefault(n, 0)
        factors[n] += 1

    res = ''

    for key in factors:
        if factors[key] == 1:
            res += f'({key})'
        else:
            res += f'({key}**{factors[key]})'
    return res

