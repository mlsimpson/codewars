# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/solutions/python

def longest(a1, a2):
    a1 = set(a1)
    a2 = set(a2)
    return "".join(list(sorted(a1.union(a2))))

print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))

