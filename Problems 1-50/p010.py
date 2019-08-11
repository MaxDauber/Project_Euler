'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
from useful_functions.mathematics import is_prime


def solution(limit):
    if limit == 2:
        return 2
    #edge cases, because after 5 the primes will all be odd, so we can increment by 2
    sum = 2+3+5
    num = 7
    while num < limit:
        if is_prime(num):
            #uncomment to list all primes below limit and show progress because this implementation is admittedly slow
            #print(str(num) + ' is prime')
            sum += num
        num += 2
    return sum


start_time = time.time()
print(solution(2000000))
print("Runtime: %s seconds" % (time.time() - start_time))
