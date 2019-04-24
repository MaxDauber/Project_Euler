'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''


#only considering largest factors that contain smaller possible factors
#ie if a number is divisible by 20 it is also divisible by 1,2 4,5,10,20
nums = [11, 13, 14, 16, 17, 18, 19, 20]

bool = False
num = 0
while not bool:
    #increment with smallest combo of prime numbers which it must include
    num += 2*3*5*7*11*13*17*19
    if num % 20 == 0:
        if num % 18 == 0:
            if num % 16 == 0:
                if num % 14 == 0:
                    bool = True
print(num)