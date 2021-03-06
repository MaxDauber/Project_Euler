'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time
from useful_functions.mathematics import sum_divisors


def solution():
    abundant_nums = []
    for num in range(1, 28123):
        if sum_divisors(num) > num:
            abundant_nums.append(num)

    nums = [i + 1 for i in range(28123)]

    # not very efficient, but it works :/
    for x in abundant_nums:
        for y in abundant_nums:
            if x + y - 1 < len(nums):
                nums[x + y - 1] = 0

    return sum(nums)


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))



