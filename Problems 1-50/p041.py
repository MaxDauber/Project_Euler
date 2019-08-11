'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
'''
NOTE:

The largest possible number that can be n-digit pandigital regardless of whether it is prime or not is 9876543210, 
because it includes every digit in their largest configuration.

Additionally, we can remember that if the digit sum is divisible by three, the whole number is divisible 
by three and as such not a prime number. Starting with 1+2+3+4+5+6+7+8+9=45, which is divisible by three. Doing the 
same without the 9 leads to 1+2+3+4+5+6+7+8=36 ,which is also divisible by three. We can check the next sum, which is 
1+2+3+4+5+6+7=28. So we can deduce that the largest pandigital number has at most 7 digits and as such is 7654321.


'''

import time
from itertools import permutations
from useful_functions.mathematics import is_prime


def solution():
    for x in list(map("".join, permutations(list("7654321")))):
        if is_prime(int(x)):
            return x

start_time = time.time()

print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))