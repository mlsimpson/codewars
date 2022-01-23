# https://www.codewars.com/kata/56606694ec01347ce800001b/solutions/python

def is_triangle(a, b, c):
	if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
		return True
	else:
		return False

