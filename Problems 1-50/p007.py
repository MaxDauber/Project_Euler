'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import time
from useful_functions.mathematics import nth_prime


def solution():
    return nth_prime(10001)


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))



