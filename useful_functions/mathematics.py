from functools import reduce
import math


# check if number is prime
def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


# finds nth prime number
def nth_prime(nth):
    if nth == 1:
        return 2
    count = 1
    num = 1
    while count < nth:
        num += 2
        if is_prime(num):
            # uncomment to see full list of primes up to desired number
            # print(str(num) + ' is prime ' + str(count))
            count += 1
    return num


# fastest known sieve algorithm for generating primes in given range
def atkin_sieve(limit):
    assert limit > 3
    sieve_list = [False] * (limit + 1)
    sieve_list[2:4] = (True, True)

    # preliminary stuff
    x = x_squared = 1
    while x_squared < limit:
        y = y_squared = 1
        while y_squared < limit:
            n = 4 * x_squared + y_squared
            if n <= limit and n % 12 in (1, 5):
                sieve_list[n] = not sieve_list[n]

            n = 3 * x_squared + y_squared
            if n <= limit and n % 12 == 7:
                sieve_list[n] = not sieve_list[n]

            if x > y:
                n = 3 * x_squared - y_squared
                if n <= limit and n % 12 == 11:
                    sieve_list[n] = not sieve_list[n]
            y += 1
            y_squared = y * y
        x += 1
        x_squared = x * x

    # remove the squares of primes (and their multiples)
    r = 5
    r_squared = r * r
    while r_squared < limit:
        if sieve_list[r]:
            for n in range(r_squared, len(sieve_list), r_squared):
                sieve_list[n] = False
        r += 1
        r_squared = r * r

    # append everything into a list
    return [x for x, p in enumerate(sieve_list) if p]



# implementation of factor-finding algorithm that runs in 0(n) = sqrt(n)
# iterates down from sqrt(n) to 1 and adds all the factors i found plus their n/i counterpart
def factors_of_reduce(num):
    return set(reduce(list.__add__, ([int(i), int(n/i)] for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0)))

# factor-finding algorithm that doesn't use reduce
def factors_of(n):
    return list((int(i), int(n/i)) for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)



# computes n_choose_r
def n_choose_r(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


# sums divisors of a specified number
def sum_divisors(num):
    sum = 0
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            if div == int(num / div):
                sum += div
            else:
                sum += div + int(num / div)
    return sum+1


# Return the multiplicative order of n(mod 10) as the multiplicative order of 10 mod an integer n relatively
# prime to 10 gives the period of the decimal expansion of the reciprocal of n
def mult_order(n):
    z = 10
    result = 1
    while z != 1:
        z = (z * 10) % n
        result += 1
    return result


# rotates input number by a given number of spots to the right
def rotate(input, shift):
    input = str(input)
    return int(input[len(input) - shift:] + input[0: len(input) - shift])