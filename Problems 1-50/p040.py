'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

'''
NOTES:
Most of my splutio n is drawn from section 5 of this paper which has an excellent proof for how to choose based on length:
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
        
These steps can be seen in the get_digit function below.

'''

def get_digit(num):
    max_range_n = num
    desired_digit = num
    containing_length = num#(9*((10**num)*(num+1)) − (10**(n+1) + 1)/9)


d = [int(digit) for digit in ''.join((str(digit) for digit in range(1, 10000001)))]
print(d[0] * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999])


ret = 1
for num in range(7):
    ret *= get_digit(10**num)
print(ret)