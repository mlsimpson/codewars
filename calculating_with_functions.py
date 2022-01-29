# so basically the operators (times, plus, minus, divided_by) would be functions
# that return another function - the function that gets returned would do the
# actual operation

# and if the number functions have an argument, they would assume that argument
# is an operator function and they would call the function with themselves
# (the number) as an argument
# def f(x):
#     def g(y):
#         return f'x = {x}, y = {y}'
#     return g

# write a make_number function so that you don’t have to define one, two, three,
# etc. each as individual functions
# one = make_number(1)
# two = make_number(2)
# three = make_number(3)
# four = make_number(4)
# five = make_number(5)
# etc.

# returned_func = f(5)
# print(returned_func(8))
# would print x = 5, y = 8
# just to illustrate the concept of functions returning functions

def zero(*args): #your code here
	if len(args) == 0:
		return 0
	else:
		return args[0](0)

def one(*args): #your code here
	if len(args) == 0:
		return 1
	else:
		return args[0](1)

def two(*args): #your code here
	if len(args) == 0:
		return 2
	else:
		return args[0](2)

def three(*args): #your code here
	if len(args) == 0:
		return 3
	else:
		return args[0](3)

def four(*args): #your code here
	if len(args) == 0:
		return 4
	else:
		return args[0](4)

def five(*args): #your code here
	if len(args) == 0:
		return 5
	else:
		return args[0](5)

def six(*args): #your code here
	if len(args) == 0:
		return 6
	else:
		return args[0](6)

def seven(*args): #your code here
	if len(args) == 0:
		return 7
	else:
		return args[0](7)

def eight(*args): #your code here
	if len(args) == 0:
		return 8
	else:
		return args[0](8)

def nine(*args): #your code here
	if len(args) == 0:
		return 9
	else:
		return args[0](9)

def plus(num_func):
	def g(outer_func):
		return outer_func + num_func
	return g

def minus(num_func):
	def g(outer_func):
		return outer_func - num_func
	return g

def times(num_func):
	def g(outer_func):
		return outer_func * num_func
	return g

def divided_by(num_func):
	def g(outer_func):
		return outer_func // num_func
	return g


print(seven(times(five()))) # -> 35
print(four(plus(nine()))) # -> 13
print(eight(minus(three()))) # -> 5
print(six(divided_by(two()))) # -> 3

