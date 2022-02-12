# https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python

def nb_year(p0, percent, aug, p):

    num_years = 0

    new_percent = percent / 100.0

    while p0 < p:
        p0 = int(p0) + int(p0 * new_percent) + aug
        num_years += 1

    print(num_years)
    return num_years

nb_year(1000, 2, 50, 1200)

