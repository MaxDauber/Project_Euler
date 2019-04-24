def isPalindrome(n):
	p = str(n)
	i1 = 0
	i2 = len(p) - 1
	while i2 > i1:
		if p[i1] != p[i2]:
            		return False
		++i1
		--i2
	return True
			



for x in range (1,999):
	for y in range(1,999):
		mult = x * y
		print(mult)
		if(isPalindrome(mult)):
			print(mult)
