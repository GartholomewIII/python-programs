import stdio
import random

n = 5

x1 = random.random()
x2 = random.random()
x3 = random.random()
x4 = random.random()
x5 = random.random()

stdio.writeln(x1)
stdio.writeln(x2)
stdio.writeln(x3)
stdio.writeln(x4)
stdio.writeln(x5)

minimum = min(x1, x2, x3, x4, x5)
maximum = max(x1, x2, x3, x4, x5)
average = (x1 + x2 + x3 + x4 + x5) / float(n)

stdio.writeln('average = ' + str(average))
stdio.writeln('minimum = ' + str(minimum))
stdio.writeln('maximum = ' + str(maximum))


