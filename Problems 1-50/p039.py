'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''



'''
NOTES:
This solution implements several forms of intuition about a right triangle:

Given (a^2 + b^2 = h^2) and (a + b + h = p)

We can see initially that b <= 500. This is because if you set a = 0, and replace h with sqrt(a^2+b^2), you can see what 
the maximum b can be given a maximum perimeter of 1000.

Next, rewriting the pythagorean theorem with h = p - a - b gives

a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab

We want to be able to reduce computational complexity, so we can manipulate the above to give b = (p^2-2pa)/(2(p-a))

If b becomes an integer, we know that any any triangle with the parameters a and p gives a pythagorean triple.

Additionally, we know that a < h and b < h. Assuming a <= b, we can see that a < p/3, so we won't check any higher.

'''

max_var = 0
max_p = 0
for p in range(2, 1000, 2):
    h = 0
    for a in range(2, int(p / 3) + 1):
        if p * (p - 2 * a) % (2 * (p - a)) == 0:
            h += 1
    if h > max_var:
        max_var = h
        max_p = p
print(max_p)



