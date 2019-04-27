'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


def nth_prime(nth):
    if nth == 1:
        return 2
    count = 1
    num = 1
    while count < nth:
        num += 2
        if is_prime(num):
            #uncomment to see full list of primes up to desired number
            #print(str(num) + ' is prime ' + str(count))
            count += 1
    return num


def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


print(nth_prime(10001))
