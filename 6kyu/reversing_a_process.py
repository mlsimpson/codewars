# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/solutions/python

def decode(r):
    cut = 0
    alpha_dict = dict(zip(range(0, 26), string.ascii_lowercase))
    #for i in alpha_dict:
        #print(i, alpha_dict[i])
    for i, char in enumerate(r):
        if char.isdigit():
            continue
        else:
            cut = i
            break
    num = r[:cut]
    code = r[cut:]
    res = ''
    for char in code:
        for i in range(0, 26):
            candidate = (i * int(num)) % 26
            if alpha_dict[candidate] == char:
                #print("match:", candidate, char)
                res += alpha_dict[i]
            else:
                continue
    if len(res) != len(code):
        return "Impossible to decode"
    return res

# best practices solutions from codewars:
#
# def decode(r):
#     i = next(i for i, c in enumerate(r) if c.isalpha())
#     n = int(r[:i]) % 26
#     if n == 13 or n % 2 == 0: return "Impossible to decode"
#     d = {ascii_lowercase[n * i % 26]: c for i, c in enumerate(ascii_lowercase)}
#     return ''.join(d[c] for c in r[i:])
#
# import re
# def decode(s) :
#     nb, s = re.findall('[0-9]+|[a-z]+', s)
#     inv = [x for x in range(26) if int(nb) * x % 26 == 1]
#     if len(inv) != 1 : return 'Impossible to decode'
#     res = ""
#     iv = inv[0]
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     for c in s:
#         res += alpha[alpha.index(c) * iv % 26]
#     return res
