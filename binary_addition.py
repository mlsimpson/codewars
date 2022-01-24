# https://www.codewars.com/kata/551f37452ff852b7bd000139/solutions/python

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary2(a, b):
	decimal_sum = a + b
	binary_array = []

	i = 0
	while(decimal_sum > 0):
		binary_array.append(decimal_sum%2)
		decimal_sum = int(decimal_sum / 2)
		i += 1

	binary_array = binary_array[::-1]

	return ''.join(str(char) for char in binary_array)

print(add_binary(10, 7))
print(add_binary2(10, 7))

