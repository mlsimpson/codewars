# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/solutions/python

# working solution, needed to refactor gap and remove get_primes
def gap(g, m, n):
    end_prime = n

    for i in range(m, n + 1):
        if is_prime(i):
            if i - end_prime == g:
                return [end_prime, i]
            end_prime = i

def is_prime(n):
    for i in range(2, int((n ** 0.5) + 1)):
        if (n % i == 0):
            return False

    return True


# First slow naive "solution"
def gap1(g, m, n):
    primes = get_primes(m, n)

    i = 0

    while i < (len(primes) - 1):
        if primes[i + 1] - primes[i] == g:
            return [primes[i], primes[i + 1]]
        i += 1

# what if i did this with a yield?
def get_primes(start, end):
    primes = []

    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)

    return primes

# solution similar to first, except with revised get_primes with a yield
def get_primes2(start, end):
    for i in range(end, start - 1, -1):
        if is_prime(i):
            yield i

def gap2(g, m, n):
    end_prime = next(get_primes2(m, n))

    for i in range(m, end_prime):
        if is_prime(i):
            if i - end_prime == g:
                return [end_prime, i]
            end_prime = i

