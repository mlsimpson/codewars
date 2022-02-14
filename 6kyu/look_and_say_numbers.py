# https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d/solutions/python
# I already had an rle encoder in snippets, just used that one

def encode_rle(s):
    counter = 0
    prev_char = s[0]
    res = ''

    for curr_char in s:
        if curr_char == prev_char:
            counter += 1
        else:
            res += str(counter) + prev_char
            prev_char = curr_char
            counter = 1

    res += str(counter) + prev_char

    return res

def look_and_say(data='1', maxlen=5):
    out = [data]

    for i in range(1, maxlen + 1):
        out.append(encode_rle(out[i - 1]))

    return out[1:]

