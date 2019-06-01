'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
import math

ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
products = []


def factors_of(n):
    return list((int(i), int(n/i)) for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)


for num in range(1,9999):
    for tuple in factors_of(num):
        number = list(str(tuple[0])+str(tuple[1])+str(num))
        if set(number) == set(ints):
            products.append(num)

print(sum(set(products)))

