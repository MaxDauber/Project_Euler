'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''


# Return the multiplicative order of n(mod 10) as the multiplicative order of 10 mod an integer n relatively
# prime to 10 gives the period of the decimal expansion of the reciprocal of n
def mult_order(n):
    z = 10
    result = 1
    while z != 1:
        z = (z * 10) % n
        result += 1
    return result


def is_prime(num):
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


longest_cycle = 7
longest = 0
for d in range(11,1000):
    if is_prime(d):
        if mult_order(d) > longest_cycle:
            longest_cycle = mult_order(d)
            longest = d
print(longest)