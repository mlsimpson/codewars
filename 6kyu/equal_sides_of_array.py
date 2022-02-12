# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/solutions/python

def find_even_index(arr):
    left_sum = 0
    right_sum = sum(arr[1:])

    if left_sum == right_sum:
        return 0

    for index, num in enumerate(arr):
        if left_sum == right_sum:
            res_index = index
            break
        if (index + 1) >= len(arr):
            res_index = -1
            break
        # print(left_sum, right_sum)
        left_sum += num
        right_sum -= arr[index + 1]

    return res_index

print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([10,-80,10,10,15,35,20]))
