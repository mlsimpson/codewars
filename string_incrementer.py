# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/solutions/python
# I made this way more complicated than it needed to be... check above url
# zfill() is useful!

# start from end of input string
# split upon first non-numeric char
def increment_string(s):
    numcount = 0
    revstr = s[::-1]
    nums = '0'
    # print(revstr)
    while len(s) > numcount and revstr[numcount].isdigit():
        numcount += 1
    # print(numcount)
    # print(outnum, numcount)
    # if numcount > 0:
    #     chars = s[:-numcount]
    #     nums = s[-numcount:]
    # else:
    #     chars = s
    #     nums = "0"
    # print(chars, nums, numcount)
    chars = s[:(len(s) - numcount)]
    nums = nums + s[len(s) - numcount:]
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

