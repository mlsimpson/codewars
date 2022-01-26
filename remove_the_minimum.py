# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/solutions/python

def remove_smallest(numbers):
    if not numbers:
        return []

    i = 0
    min = numbers[0]
    min_index = 0

    while i < len(numbers):
        if numbers[i] < min:
            min = numbers[i]
            min_index = i

        i += 1

    out = numbers[:min_index] + numbers[min_index + 1:]

    return out


print(remove_smallest([1, 2, 3, 4, 5]))

