# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/solutions/python

def sort_array(source_array):

    out = []
    evens = [x for x in source_array if x % 2 == 0]
    odds = sorted([x for x in source_array if x % 2 != 0])

    # print(odds)

    for x in source_array:
        if(x % 2 == 0):
            out.append(evens.pop(0))
        else:
            out.append(odds.pop(0))

    return out


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))



