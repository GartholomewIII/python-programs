#---------------------------------------------------------------------
# Quinn Olney 9/6/2024 windchill.py 
#----------------------------------------------------------------------

import stdio 
import math 
import sys 

#Here I am taking the temperature and speed of wind by using the built in input function which allows you 
#to ask for input from the command line which makes it more user readable

t = float(sys.argv[1])
v = float(sys.argv[2])

#Then down below we are taking the equation that calculates the windchill, I used the ** operand which is a built in
#python function for exponents

m = 35.74 + (0.6215 * t) + (0.4275 * t - 35.75) * (v ** 0.16)

#finally we output it with a user readable message

stdio.writeln('Your windchill is ' + str(m))

