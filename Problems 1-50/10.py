'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def sum_primes(limit):
    if limit == 2:
        return 2
    #edge cases, because after 5 the primes will all be odd, so we can increment by 2
    sum = 2+3+5
    num = 7
    while num < limit:
        if is_prime(num):
            #uncomment to list all primes below limit and show progress because this implementation is admittedly slow
            #print(str(num) + ' is prime')
            sum += num
        num += 2
    return sum


def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


print(sum_primes(2000000))
