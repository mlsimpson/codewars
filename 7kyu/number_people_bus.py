# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/solutions/python

def number(bus_stops):
    num_people = 0

    for pair in bus_stops:
        num_people += pair[0]
        num_people -= pair[1]

    return num_people
