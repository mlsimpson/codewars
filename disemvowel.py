# https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/python/all/best_practices

def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    newstring = ""

    for char in string:
        if char not in vowels:
            # print(char)
            newstring += newstring.join(char)

    print(newstring)

disemvowel("This website is for losers LOL!")
