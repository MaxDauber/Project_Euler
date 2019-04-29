'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


# NOTE:I really enjoy combinatorics problems and this is a perfect problem that helped me understand the idea of
# choosing. If you take an NxN grid, you are going to have to take some combination of R (go right) and D (go down) to
# reach the bottom right corner. For example for the 2x2 grid you can have RDRD, RRDD, DDRR, DRDR, RDDR, DRRD. As long
# as the number of Rs equals the number of Ds for any N > 1, you will reach the bottom right, and the formula to find
# number of combinations is simply (2N choose N) which equates to choose half of the distances to be R and half to be D

import math


def n_choose_r(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print(n_choose_r(40, 20))
