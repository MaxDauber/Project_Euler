'''
Let big_num(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If big_num(a) = b and big_num(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore big_num(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so big_num(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import time
from useful_functions.mathematics import sum_divisors

def solution():
    amicable_sum = 0
    amicable = []
    for x in range(2, 10001):
        if sum_divisors(sum_divisors(x)) == x and x != sum_divisors(x) and x not in amicable:
            amicable.append(x)
            amicable.append(sum_divisors(x))
            amicable_sum += x + sum_divisors(x)

    return amicable_sum


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))
