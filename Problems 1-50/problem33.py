'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from fractions import Fraction

product = 1

for i in range(10,100):
    for j in range(i+1,100):
        common = list(set(str(i))&set(str(j)))
        num = list(str(i))
        den = list(str(j))
        if len(common) != 0:
            if common[0] != '0':
                num.remove(common[0])
                den.remove(common[0])
                if num[0] != '0' and den[0] != '0':
                    if Fraction(i, j) == Fraction(int(num[0]), int(den[0])):
                        product *= Fraction(i, j)

print(product.denominator)
