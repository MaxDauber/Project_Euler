'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
'''
NOTES:
This solution uses brute force (super lame, I know) but a more elegant and interesting solution can be found in this paper:
https://artemlos.net/docs/2014/01/MathExploration.pdf

The procedure is:
1. Choose what interval the solution needs to be in (what length number the solution rests in), for example for digit 
number 206788, we can see that 206788 < 488889 which is the upper bound on digits for numbers with length of 5, so we 
can see that the desired digit will be in a 5-digit number

2. We use the derived formula with our specifications inserted to find the number that contains the digit:

        10^containing_length - 1 - floor(ceiling((max_range_n - desired_digit)/containing_length))
        
        For example: desired_digit=206788 -> max_range_n=488889, containing_length=5 -> 99999 − floor(56420.2) -> num 
        with digit = 43579

3. Now that we know the number with our digit, we can find which digit it is by looking at the remainder, or more 
specifically (g(⌈a⌉)− g(a)) mod n where n is the length of the number containing the digit. 

        For example: (488889 - 206788) % 5 -> 1 which means that the desired digit is 7. Notice that the digit count is 
        from right to left, i.e. if the remainder would be zero, the digit would be 9, and so on.

'''
import time


def solution():
    big_num = [int(digit) for digit in ''.join((str(digit) for digit in range(1, 10000001)))]
    return big_num[0] * big_num[9] * big_num[99] * big_num[999] * big_num[9999] * big_num[99999] * big_num[999999]

start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))


