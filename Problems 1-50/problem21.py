'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

#sums divisors of a specified number
def sum_divisors(num):
    sum = 0
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            if div == int(num / div):
                sum += div
            else:
                sum += div + int(num / div)
    return sum+1

amicable_sum = 0
amicable = []
for x in range(2, 10001):
    if sum_divisors(sum_divisors(x)) == x and x != sum_divisors(x) and x not in amicable:
        amicable.append(x)
        amicable.append(sum_divisors(x))
        amicable_sum += x + sum_divisors(x)

print(amicable_sum)
