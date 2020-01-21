'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time
from useful_functions.mathematics import atkin_sieve

primes = atkin_sieve(10000)
set_primes = set(primes)

def solution():
    return primes





start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))