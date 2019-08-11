'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time

memo = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def solution():
    sum = 0
    for num in range(3, 100000):
        tempsum = 0
        for x in list(str(num)):
            tempsum += memo[int(x)]
        if tempsum == num:
            sum += num
    return sum


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))