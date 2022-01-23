# https://www.codewars.com/kata/55c45be3b2079eccff00010f/solutions/python

def order(sentence):
    if sentence == "":
        return ""

    sentence = sentence.split()

    # Parse words for number
    # compare number against other numbers
        # data structure what inserts based on number sort
        # could be [number, word]
    # rearrange sentence based on number sort

    words = []

    for word in sentence:
        # Numbers can be from 1 to 9. So 1 will be the first word (not 0).
        for char in word:
            if char.isnumeric():
                words.append([char, word])

    # print(words)

    words = sorted(words, key=lambda x: x[0])

    # print(words)

    res = ' '.join(word[1] for word in words)
    print(res)
    return res

order("is2 Thi1s T4est 3a")

