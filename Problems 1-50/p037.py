'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

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

# check if number is two
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

# check if number is prime
def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


primes = atkin_sieve(1000001)
truncatables = []
prime_additions = [2,3,5,7]
# starting at 10
index = 2
while len(truncatables) < 11:
    # print(primes[index])
    if is_two_sided(primes[index]):
        truncatables.append(primes[index])
    index += 1

print(sum(truncatables))
