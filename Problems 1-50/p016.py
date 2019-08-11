'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import time


def solution():
    return sum(int(loc) for loc in str(int(2**1000)))


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))

