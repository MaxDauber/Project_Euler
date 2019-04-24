'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(n):
    p = str(n)
    i1 = 0
    i2 = len(p) - 1
    while i2 > i1:
        if p[i1] != p[i2]:
            return False
        i1 += 1
        i2 -= 1
    return True

largest = 0
for x in range(1, 999):
    for y in range(1, 999):
        mult = x * y
        if (isPalindrome(mult) and mult > largest):
            largest = mult
print(largest)
