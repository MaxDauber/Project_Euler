'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

import time
from useful_functions.mathematics import atkin_sieve, factors_of
from math import sqrt

primes = atkin_sieve(10000)
set_primes = set(primes)

def solution():
    for num in range(1000, 1000000):
        if len(prime_factors_of(num)) == 4:
            if len(prime_factors_of(num + 1)) == 4:
                if len(prime_factors_of(num + 2)) == 4:
                    if len(prime_factors_of(num + 3)) == 4:
                        return num

def prime_factors_of(n):
    prime_factors = set()
    while n % 2 == 0:
        prime_factors.add(2)
        n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
    for prime in primes:
        while n % prime == 0:
            prime_factors.add(prime)
            n = n / prime
        if prime >= n:
            break
    return prime_factors

start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))