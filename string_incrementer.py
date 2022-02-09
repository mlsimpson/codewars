# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/solutions/python
# I made this way more complicated than it needed to be... check above url
# zfill() is useful!

def increment_string_wrong(s):
    outchars = ''
    outnum = '0'
    numcount = 0
    for char in s:
        if char.isalpha():
            outchars += char
        else:
            numcount += 1
            outnum += char

    print(outchars, outnum)

    outnum = int(outnum) + 1

    padding = ''

    numpad = len(str(outnum)) - 1

    # print(len(str(outnum)), numcount)
    if len(str(outnum)) < numcount:
        while numpad < (numcount - 1):
            padding += '0'
            numpad += 1

    # print(padding)

    # if len(padding + str(outnum)) > numcount:
    #    padding = padding[1:]

    # print(padding)

    print(s)

    # print(outchars + " " + padding + " " + str(outnum))
    # print("numcount:", numcount)

    return (outchars + padding + str(outnum))

# start from end of input string
# split upon first non-numeric char
def increment_string(s):
    numcount = 0
    revstr = s[::-1]
    # print(revstr)
    while len(s) > numcount and revstr[numcount].isnumeric():
        numcount += 1
    # print(numcount)
    # print(outnum, numcount)
    if numcount > 0:
        chars = s[:-numcount]
        nums = s[-numcount:]
    else:
        chars = s
        nums = "0"
    # print(chars, nums, numcount)
    final_num = str(int(nums) + 1)

    # print(len(final_num), numcount)
    if len(final_num) < numcount:
        # print('0' * (numcount - len(final_num)) + final_num)
        final_num = ('0' * (numcount - len(final_num)) + final_num)
    return (chars + final_num)

print(increment_string("fYkCBwOnCCp0%{#)2870<($02592142?079000000629719169"))
print(increment_string("foo"))
print(increment_string(""))
print(increment_string("123"))

