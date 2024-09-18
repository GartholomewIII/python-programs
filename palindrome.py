#--------------------------------------------------------------------------
# Quinn Olney 9/9/2024 palindrome.py
#-------------------------------------------------------------------------

import stdio 
import sys

#Here I am taking the users input and then having a seperate variable for removed whitespace/punctuation and 
#capitalization

user_string = str(sys.argv[1])
remove_whitespace = "".join(user_string.split())

#----------------------REMOVING CAPITALIZATION--------------------------------
#here the capitalization is being removed using the lower function
remove_whitespace = remove_whitespace.lower()
    
# ----------------------REMOVING PUNCUTATION---------------------------------
#then using a simple for look we iterate thrugh the string and if it is in the punc variable 
#it is removed using the replace function
punc = "!()-[];:\,<>./?@#$%^&*_~"

for ele in remove_whitespace:
    if ele in punc:
        remove_whitespace = remove_whitespace.replace(ele, "")



#Then we reverse both strings
reverse_str_ws = remove_whitespace[::-1]
reverse_str = user_string[::-1]


#if the basic input from the user is the exact same reversed then it is an exact palindrome
if user_string == reverse_str:
    stdio.writeln('This is a exact palindrome')
#if the first condition isn't satisfied then we compare the reversed string with no punctuation, capitalization
#and whitespace to the reversed version of it
elif remove_whitespace == reverse_str_ws:
    stdio.writeln('This is an inexact palendrome')
#if the first two conditions aren't met then it cannot be a palindrome
else:
    stdio.writeln('This is not a palendrome')

