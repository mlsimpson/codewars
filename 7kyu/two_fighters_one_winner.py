# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/solutions/python

def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        first = fighter1
        second = fighter2
    else:
        first = fighter2
        second = fighter1

    while 1:
        second.health -= first.damage_per_attack
        if second.health < 1:
            return first.name
        first.health -= second.damage_per_attack
        if first.health < 1:
            return second.name

