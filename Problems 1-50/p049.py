'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:

(i) each of the three terms are prime
(ii) each of the 4-digit numbers are permutations of one another

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time
from useful_functions.mathematics import atkin_sieve


primes = atkin_sieve(10000)
set_primes = set(primes)

def solution():
    four_digit_primes = filter(lambda x : 1000 < x < 10000 , set_primes)

    return four_digit_primes



start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))