#------------------------------------------------------------------------------------------------------------
# Quinn Olney 9/16/2024 twodice.py
#------------------------------------------------------------------------------------------------------------
import stdio 
import math
import random
import stdarray
import sys

#-----------------------collecting the liklihood of each die-----------------------

probabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1.0 #given algorithm to calculate the chances for each dice roll
for k in range(2, 13):
    probabilities[k] /= 36.0

#-----------------------outputting it through a simple for loop----------------------------------
#here I am outputting it, using concanation I can just use i to get which dice number is represented by the data 
#instead of having to create a if elif branch that is redundant
stdio.writeln("Exact Results")
for i in range(len(probabilities)):
    stdio.writeln("Probability the sum of die is " + str(i + 2) + ' :' + str(probabilities[i +2]))

    if i + 3 == len(probabilities):
        break

#--------------------collecting the random possibilities--------------------------------------
#now we get to the good part, we take the amount of dice rolls from user input using the sys module
#then we create a 11 char long array with 0 as the place holder
#then we initialize temp_rand_one and two which will get reassigned a new value each loop for each
#dice roll

test_case_num = int(sys.argv[1])
test_case_data = stdarray.create1D(11, 0)
temp_rand_one = 0
temp_rand_two = 0

#here we are simply looping for the amount of dice rolls needed
#each loop we get two random ints one for temp_rand_one and the other for two using the random randrange function

#
for i in range(test_case_num):
    temp_rand_one = random.randrange(1,7)
    temp_rand_two = random.randrange(1,7)

#then we check if the two values sum up to each individual possible combination 
#if we roll two ones and it sums to 2 we incriment the index in test_case_data that represents the roll
#in this case 2 = 0, 3 = 1, etc

    if temp_rand_one + temp_rand_two == 2:
        test_case_data[0] += 1
    elif temp_rand_one + temp_rand_two == 3:
        test_case_data[1] += 1 
    elif temp_rand_one + temp_rand_two == 4:
        test_case_data[2] += 1
    elif temp_rand_one + temp_rand_two == 5:
        test_case_data[3] += 1 
    elif temp_rand_one + temp_rand_two == 6:
        test_case_data[4] += 1
    elif temp_rand_one + temp_rand_two == 7:
        test_case_data[5] += 1 
    elif temp_rand_one + temp_rand_two == 8:
        test_case_data[6] += 1
    elif temp_rand_one + temp_rand_two == 9:
        test_case_data[7] += 1 
    elif temp_rand_one + temp_rand_two == 10:
        test_case_data[8] += 1 
    elif temp_rand_one + temp_rand_two == 11:
        test_case_data[9] += 1
    elif temp_rand_one + temp_rand_two == 12:
        test_case_data[10] += 1 
#--------------------------------outputting the possibilites to sandard output \--------------------------
#we output this using a simple for loop and the same method above
stdio.writeln('------------------------------------------------------------------')
stdio.writeln("Empirical results")

for i in range(len(test_case_data)):
    test_case_data[i] = test_case_data[i] / float(test_case_num)
    stdio.writeln("Results the sum of die is " + str(i+2) + ' :' + str(test_case_data[i]))


#----------------------------------getting the difference-----------------------------------------------------
#finally we calculate the difference
stdio.writeln('-------------------------------------------------------------------')
stdio.writeln('difference')
difference = stdarray.create1D(11,0)

#since the probabilities data type has two 0's at the beginning it's two indexes longer than both difference and test_case_data
#because of that we need to slice these two first points out using list comprehension 
#then we simply take the data representing the probability for a dice roll and subtract the actual test case data
#we update the index representing this roll in the difference array and if i +2 == 12 (out of the probability index range) we break 
for i in range(len(probabilities[2::])):
    difference[i] = probabilities[i +2] - test_case_data[i]

    if i +2 == 12:
        break
#finally we recycle the for loop used above for test_case_data to output the difference

for i in range(len(difference)):
    stdio.writeln("Results the sum of die is " + str(i+2) + ' :' + str(round(difference[i], 6)))

#n or in this case test_case_num needs to be approx 200,000 dice rolls until it is accurate to 3 decimal places
#it gets close when n approaches 100,000 but doesn't quite reach it until then