# https://www.codewars.com/kata/54ba84be607a92aa900000f1/solutions/python

def is_isogram(string):
    out = set()

    for char in string.lower():
        out.add(char)

    return len(string) == len(out)

print(is_isogram("aba"))
