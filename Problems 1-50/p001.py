'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time


def solution():
    sum = 0
    for i in range(999):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))