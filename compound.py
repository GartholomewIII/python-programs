#-------------------------------------------------------------
# Quinn Olney 9/6/24 Compound Interest Function
#------------------------------------------------------------

import stdio 
import math
import sys

#collecting the variables from command line input for the equation
#y = p * e^(t*r), t represents time passed, r is the rate of compounding and p is the principal

t = int(sys.argv[1])
p = int(sys.argv[2])
r = float(sys.argv[3])

#here we're using the math.exp method which takes e^x or the input in the parenthesis, and then we multiply it by 
#the principal, after that I use the round method which takes two arguments (x,y) x= the number to be rounded 
#and y what decimal place it rounds to 

result = round(p * (math.exp(r*t)), 2)

#finally we output it to the command line using the standard io library

stdio.writeln('Your total would be ' + str(result))