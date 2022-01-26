# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/solutions/python

def validate_pin(pin):
    out = []
    for i in pin:
        if i == '-':
            return False
        if i == '.':
            return False
        if not i.isnumeric():
            return False
        else:
            out.append(i)

    return len(out) == 4 or len(out) == 6
