# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/solutions/python

def is_pangram(s):
    s_set = {char.lower() for char in s if char.isalpha()}
    return (len(s_set) == 26)

print(is_pangram("58095$##The quick brown fox jumps over the lazy dog"))
print(is_pangram("a53jk5ljkfdsajkbajbdakckekeldaifdl"))

