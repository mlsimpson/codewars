# https://www.codewars.com/kata/57814d79a56c88e3e0000786/solutions/python

def decrypt(encrypted_text, n):
    if not encrypted_text:
        return encrypted_text

    res = encrypted_text

    while n > 0:
        evens = []
        odds = []
        tmp_text = ''

        for index, char in enumerate(res):
            if index < (len(res) // 2):
                evens.append(char)
            else:
                odds.append(char)

        for i in range(len(encrypted_text)):
            if i % 2 == 0:
                tmp_text += odds.pop(0)
            if i % 2 != 0:
                tmp_text += evens.pop(0)
        res = ''.join(tmp_text)
        n -= 1

    return res

def encrypt(text, n):
    if not text:
        return text

    res = text

    while n > 0:
        evens = []
        odds = []

        for index, char in enumerate(res):
            if index % 2 == 0:
                evens.append(char)
            else:
                odds.append(char)
            res = ''.join(odds + evens)
        n -= 1

    return res

