# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/solutions/python

def tower_builder(n_floors):
    rows = []

    for i in range(n_floors):
        row = [' '] * ((n_floors * 2) - 1)
        middle = len(row) // 2

        for j in range(middle - i, middle + i + 1):
            row[j] = '*'
            res = ''.join(row)

        rows.append(res)

    return rows

