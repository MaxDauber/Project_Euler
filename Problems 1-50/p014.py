'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''
import time


# recursive function to find the length of the sequence according to above rules
def find_length(n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return 1 + find_length(n / 2)
    else:
        return 1 + find_length(3*n+1)


def solution():
    largest = 0
    num = 0
    for i in range(1, 1000000):
        seq = find_length(i)
        if seq > largest:
            largest = seq
            num = i
    return num


start_time = time.time()
print(solution())
print("Runtime: %s seconds" % (time.time() - start_time))





