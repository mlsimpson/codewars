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


