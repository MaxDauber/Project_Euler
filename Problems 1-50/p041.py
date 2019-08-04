'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
'''
NOTE:

The largest possible number that can be n-digit pandigital regardless of whether it is prime or not is 9876543210, 
because it includes every digit in their largest configuration.



'''

import time
from useful_functions.mathematics import atkin_sieve


def solution():
    for num in reversed(atkin_sieve(9876543210)):
        print(num)
        if set(list(str(num))) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return num


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))