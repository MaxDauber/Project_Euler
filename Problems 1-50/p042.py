'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt, how many are triangle words?
'''

'''
NOTE:

The formula for finding a triangular number is t = ½n(n+1), so we want to get the inverse function so that the check 
takes O(1) instead of having to iterate over triangular numbers to get to n. 

The result is n = sqrt(1 + 8 * (sum of letter numbers or t)) - 1) / 2

'''


import time
from math import sqrt

def get_matching(str):
    alpha_ord = lambda c: ord(c.lower()) - ord('a') + 1
    return sum(map(alpha_ord, str))


def is_triangular(str):
    num = ((sqrt(1 + 8 * get_matching(str)) - 1) / 2.0)
    if num == int(num):
        return True
    return False


def solution():
    with open('p042_words.txt') as file:
        name_list = file.read().split(',')
        num_words = 0
        for word in name_list:
            if is_triangular(word.strip('\"')):
                num_words += 1
        return num_words

start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))