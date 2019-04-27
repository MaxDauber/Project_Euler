'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

div = 600851475143
largest = 0
for i in range(3, int(math.sqrt(div))+1, 2):
        # while i divides n , print i ad divide n 
        while div % i == 0:
            largest = i
            div = div / i
print(largest)