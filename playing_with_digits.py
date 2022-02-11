#

def dig_pow(n, p):
    n_list = list(map(int, str(n)))
    res = 0

    for num in n_list:
        res += (num ** p)
        p += 1

    return int(res / n) if (res / n) % 1 == 0 else -1

