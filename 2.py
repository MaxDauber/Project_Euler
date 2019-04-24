sum = 0
x = 1
y = 2
while(y < 4000000):
	if y % 2 == 0:
		sum += y
	z = (x + y)
	x = y
	y = z
print(sum)
