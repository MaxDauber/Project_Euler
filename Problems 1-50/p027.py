'''
Euler discovered the remarkable quadratic formula: n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when
n=40,40^2+40+41=40(40+1)+41 n is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The
product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000 where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
primes for consecutive values of n, starting with n=0
'''
import time
from useful_functions.mathematics import is_prime


def quadratic_prime_producer(a_lim, b_lim):
    longest = [0, 0, 0]
    for a in range((a_lim * -1) + 1, a_lim):
        for b in range(2, b_lim):
            if is_prime(b):
                count = 0
                n = 0
                while is_prime((n**2) + (a*n) + b):
                    count += 1
                    n += 1

                if count > longest[0]:
                    longest = [count, a, b]

    return longest


def solution():
    ans = quadratic_prime_producer(1000, 1000)
    return ans[1] * ans[2]


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))

