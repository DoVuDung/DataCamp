#number list
number = [1,2,3]
#Import nump
import numpy as np
#creare condition array
condition = np.array(number > 1)
#print number
print(number)
#print condition
print(condition)
#print numbers greatter 1
print(number[condition])
