#AskForRNG Project
#
# Project Objectives
#   ask for input and do somthing with it 
#   if (else) and while conditions
#   
# TO-DO/Improvements
#   create specific parameters for wrong input
#   




#Input
RNGprompt = str(input("Would you like a random number? respond with y or n \n  "))

#Actual Random Number Generator 
import random
x = random.randint(1, 100)

#Output
while RNGprompt == "y":
    print("Okay! Here's a random number:",x)
    RNG = str(input("Would you like another random number?"))
    x = random.randint(1, 100)
else:
    print("Aww okay...")