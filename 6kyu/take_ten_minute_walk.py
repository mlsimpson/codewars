# https://www.codewars.com/kata/54da539698b8a2ad76000228/solutions/python

def is_valid_walk(walk):
	if len(walk) < 10 or len(walk) > 10:
	    return False
	ns = 0
	ew = 0
	for char in walk:
	    if char == 'n':
	        ns += 1
	    if char == 's':
	        ns -= 1
	    if char == 'e':
	        ew += 1
	    if char == 'w':
	        ew -= 1
	return (ns == 0) and (ew == 0)

print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
