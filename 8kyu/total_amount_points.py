# https://www.codewars.com/kata/5bb904724c47249b10000131/solutions/python

def points(games):
    wins = 0
    for i in games:
        if i[0] > i[2]:
            wins += 3
        elif i[0] < i[2]:
            wins -= 0
        else:
            wins += 1

    return wins

