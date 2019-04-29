'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
'''

sum = 1000;

for a in range(1,int(sum/3+1)):
    for b in range(a + 1, int(sum/2+1)):
        #do not need to calculate value for c because there will only be one that fits
        c = sum - a - b
        if a*a + b*b == c*c:
            print('a=' + str(a))
            print('b=' + str(b))
            print('c=' + str(c))
            print('a*b*c=' +str(a*b*c))
