'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import time
from itertools import permutations

def solution():
    counter = 1
    for permutation in permutations([i for i in range(10)], 10):
        if counter == 1000000:
            ret = ''
            for i in list(permutation):
                ret += str(i)
            return ret
        counter += 1


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))


