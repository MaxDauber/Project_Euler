'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import time
from useful_functions.mathematics import is_prime, atkin_sieve, rotate


def solution(limit):
    circ_num = 0
    primes = atkin_sieve(limit)
    for num in primes:
        add = True
        for i in range(len(str(num))):
            if not is_prime(rotate(num, i)):
                add = False
        if add:
            circ_num += 1
    return circ_num


start_time = time.time()
print(solution(1000000))
print("Runtime: %s seconds" % (time.time() - start_time))

