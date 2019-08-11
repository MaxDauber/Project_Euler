'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import time
from math import factorial


def solution():
    return sum(int(x) for x in list(str(factorial(100))))


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))
