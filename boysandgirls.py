#------------------------------------------------------------------------------------------------------
# Quinn Olney 9/13/2024 boysandgirls.py
#-------------------------------------------------------------------------------------------------------
import stdio 
import stdarray 
import random 
import math 
import sys

#first we import the library we're going to need
#then we initialize our counter variables

#----------- COUNTER VARIABLEs ------------------
trial_num = int(sys.argv[1])

#taking a command line argument for how many trials ^^

two_count = 0 
three_count = 0 
four_count = 0
five_more = 0 

#counters for how many children it takes to get both a boy and a girl ^

temp_children = stdarray.create1D(0)

#creating an empty array to append results into and then use the built-in 'in' function that checks if we 
#reached our exit condition, that is, it checks if there is both a boy and a girl in there

for i in range(trial_num):
    #we want to loop for the amount of trials
    #boygirl = false because in our current testcase we haven't met our requirement
    boygirl = False
    while boygirl == False:

    #then we only enter this while loop when temp_children does not have a boy and a girl 
        if random.randrange(0,2) == 0:
            temp_children.append('boy')
        else:
            temp_children.append('girl')

    #Here we are generating a random int, either 0 or 1, if zero we append boy if other girl intp temp_children

        if 'boy' in temp_children and 'girl' in temp_children:

    #here we check if both boy and girl is in temp_children, if not continue
    
            if len(temp_children) == 2:
                two_count += 1
            elif len(temp_children) == 3:
                three_count += 1 
            elif len(temp_children) == 4:
                four_count += 1 
            elif len(temp_children) >= 5:
                five_more += 1
            temp_children = []
            boygirl = True
            break 
            #then this section is simply taking the len of temp_children (the amount of children it took to reach #exit condition) and adding to it's respective counter, then we set temp children back to an empty array and set boygirl to True so it exits the while loop and then break just in case


average_children = round(sum([two_count * 2, three_count * 3, four_count * 4, five_more * 5]) / float(trial_num))

#finally we need to get the average, to do this we get the weighted quantity of each variable
#ie how many attempts to get two children times two the we divide the total amount of children
#by the number of trials and then around it

stdio.writeln('average # of children: ' + str(average_children))

stdio.writeln("trials with two children: " + str(two_count))
stdio.writeln("trials with three children: " + str(three_count))
stdio.writeln("trials with four children: " + str(four_count))
stdio.writeln("trials with five or more children: " + str(five_more))

#then we output the results