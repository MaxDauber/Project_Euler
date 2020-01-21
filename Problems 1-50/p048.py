'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

import time, math
from useful_functions.mathematics import atkin_sieve

primes = atkin_sieve(10000)
set_primes = set(primes)

def solution():
    for num in range(1, 100):
        print(num, find_ones_congruency(num), math.pow(num, num) % 10)




def find_ones_congruency(num):
    for pow in range(1, num + 1):
        rem = math.pow(num, pow) % 10
        #print(rem, num, pow, math.pow(num, pow))
        if rem == 1:
            return 1, pow
        if rem == -1:
            return -1, pow
    return None





start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))