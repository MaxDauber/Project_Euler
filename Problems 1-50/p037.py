'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time
from useful_functions.mathematics import atkin_sieve


primes = atkin_sieve(1000001)
truncatables = []
prime_additions = [2, 3, 5, 7]

# check if number is two sided
def is_two_sided(n):
    ret = True
    num = n
    if num > 10:
        # checking left
        for x in range(len(str(num))):
            if int(num) not in primes:
                ret = False
            num = str(num)[1:]
        num = n
        # checking right
        for x in range(len(str(num))):
            if int(num) not in primes:
                ret = False
            num = str(num)[:-1]
        return ret
    else:
        return False

def solution():
    # starting at 10
    index = 2
    while len(truncatables) < 11:
        # print(primes[index])
        if is_two_sided(primes[index]):
            truncatables.append(primes[index])
        index += 1
    return sum(truncatables)


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))

