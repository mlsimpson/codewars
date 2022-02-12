# codewars.com/kata/57b06f90e298a7b53d000a86/solutions/python

def queue_time(customers, n):
    if not customers:
        return 0

    if n > len(customers):
        n = len(customers)

    tills = [0] * n

    for cust in customers:
        tills[0] += cust
        # or: tills[tills.index(min(tills))] += cust
        tills.sort()

    return max(tills)

