# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/solutions/python

def human_years_cat_years_dog_years(human_years):
    # return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]
    cat = 0
    dog = 0

    index = 1
    while index <= human_years:
        if index == 1:
            cat += 15
            dog += 15
        elif index == 2:
            cat += 9
            dog += 9
        else:
            cat += 4
            dog += 5
        index += 1

    return [human_years, cat, dog]

