# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/solutions/python
import functools

def fib(nth):
    two_before = 0
    one_before = 1
    index = 0

    while(index < nth):
        new_one_before = two_before + one_before
        two_before, one_before = one_before, new_one_before
        index += 1

    return two_before

@functools.lru_cache
def productFib(prod):
	# HACKY OH GOD
	if prod == 0:
		return [0, 1, True]
	fn = 0
	fn1 = 0
	iteration = 1
	while fn * fn1 < prod:
		fn = fib(iteration)
		fn1 = fib(iteration + 1)
		if fn * fn1 == prod:
			return [fn, fn1, True]
		iteration += 1
	return [fn, fn1, False]


print(productFib(4895))
