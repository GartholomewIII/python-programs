import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

minimum = min(a, b, c)
maximum = max(a, b, c)
median = (a + b + c) - minimum - maximum

stdio.writeln(minimum)
stdio.writeln(maximum)
stdio.writeln(median)
