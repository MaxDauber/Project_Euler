'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import time


def solution():
    sum = 0
    squared_sum = 0
    for i in range(1, 101):
        sum += i
        squared_sum += i * i
    return sum * sum - squared_sum


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))



