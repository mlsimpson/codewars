# https://www.codewars.com/kata/54dc6f5a224c26032800005c/solutions/python

def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ""

    counts_per_art = {}

    for cat in listOfCat:
        counts_per_art[cat] = 0

    for art in listOfArt:
        count = art.split()[1]
        cat = art.split()[0][0]
        if cat in counts_per_art:
            counts_per_art.setdefault(cat, 0)
            counts_per_art[cat] += int(count)

    res = ' - '.join("(" + stock + " : " + str(counts_per_art[stock]) + ")" for stock in counts_per_art)
    return res

