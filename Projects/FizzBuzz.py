#THis is the code that I have for the fizz buzz problem/exercise for Python course. 

#1. Program should print each number from 1 - 100 in a turn sequence.

#2. Need to check if any input is divisible by a number if a number is divisible by the following: 

#   3 print "Fizz"
#   5 print "Buzz"
#   If both 3 and 5 print "FizzBuzz"

##Minor note each input should print on a new line. 


for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0: 
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (f"{i}")
