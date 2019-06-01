'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

from timeit import default_timer as timer
start = timer()

# caching powers of 5 for 0(1) access
fifthPowers = []
for i in range(10):
    fifthPowers.append(int(i**5))

sum = 0
for num in range(2, 355000):
    sum_of_digits = 0
    number = num
    for x in str(num):
        sum_of_digits += fifthPowers[int(x)]
    if num == sum_of_digits:
        sum += sum_of_digits

elapsed_time = (timer() - start) * 100

# print("Time: " + str(elapsed_time))
print(sum)
