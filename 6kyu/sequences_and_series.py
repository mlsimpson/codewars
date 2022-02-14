# https://www.codewars.com/kata/5254bd1357d59fbbe90001ec/solutions/python
# oh geez...
# 50*(n*(n+1))/2

def get_score(n):
    score = 0
    index = 1

    while index <= n:
        score += (50 * index)
        index += 1

    return score

