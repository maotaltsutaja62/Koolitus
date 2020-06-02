import math
number = 20
for x in range (number):
    if x == 0:
        continue
    
    elif x%2 ==0:#% võtab jäägi,kui on 0,siis on paarisarv
        print(math.sqrt(x))
    else:
        print(x**2)
        
