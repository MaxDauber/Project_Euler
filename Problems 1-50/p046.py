'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import time
from useful_functions.mathematics import atkin_sieve

primes = atkin_sieve(10000)
set_primes = set(primes)

# odd composite numbers are odd numbers excluding the primes (in other words the ones that have factors)
odd_composites = list(set(2 * num + 1 for num in range(1, 10000)).difference(set_primes))
twice_squares = set(2 * num * num for num in range(1, 10000))

def solution():
    print(primes)
    print(odd_composites)
    print(twice_squares)
    for num in odd_composites:
        found = False
        for prime in primes:
            print(num, prime)
            if prime > num:
                break
            if num - prime in twice_squares:
                found = True
        if not found:
            return num

start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))