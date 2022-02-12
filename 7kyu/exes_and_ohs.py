# https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python
# don't forget string.count('char') !

def xo(s):
    os = []
    xs = []

    for char in s.lower():
        if char == 'x':
            xs.append(char)
        elif char == 'o':
            os.append(char)
        else:
            continue

    return len(xs) == len(os)

