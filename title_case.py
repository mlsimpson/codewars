# https://www.codewars.com/kata/5202ef17a402dd033c000009/solutions/python

def title_case(title, minor_words=''):
    if not title:
        return ''

    allwords = title.split()
    allwords_upper = [word.upper() for word in title.split()]
    minor_upper = [word.upper() for word in minor_words.split()]

    index = 1
    out = []
    out.append(allwords[0].title())

    while index < len(allwords):
        if allwords_upper[index] not in minor_upper:
            out.append(allwords[index].title())
        else:
            out.append(allwords[index].lower())
        index += 1

    return ' '.join(out)

