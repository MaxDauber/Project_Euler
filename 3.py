import math
div  = 600851475143
for i in range(3,int(math.sqrt(div))+1,2): 
          
        # while i divides n , print i ad divide n 
        while div % i== 0: 
            print (i) 
            div = div / i 
