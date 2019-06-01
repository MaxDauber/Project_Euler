'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import math, time


# fastest known sieve algorithm for generating primes in given range
def sieve_of_atkin(limit):
    P = [2,3]
    sieve = [False]*(limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4*x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5): sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n % 12 == 7: sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 12 == 11: sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p]: P.append(p)
    return P


# generic prime checking algorithm
def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


# rotates input number by a given number of spots to the right
def rotate(input, shift):
    input = str(input)
    return int(input[len(input) - shift:] + input[0: len(input) - shift])


start = time.time()


# solves problem description using above methods
def circ_primes(limit):
    circ_num = 0
    primes = sieve_of_atkin(limit)
    for num in primes:
        add = True
        for i in range(len(str(num))):
            if not is_prime(rotate(num, i)):
                add = False
        if add:
            circ_num += 1
    return circ_num


print(circ_primes(1000000))
end = time.time()
# print(end - start)
