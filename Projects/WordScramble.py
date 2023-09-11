#Import the needed libraries to do the job
import random
import string 


#define something to stor the variables for strings 
gen_string = string.ascii_letters

#something to put all of the values of the string 
final_string= " "
random_table = []

#catch user input
user_input = int(input("How many words do you want to scramble? "))

#write loop for character selection based on user input
for char in range(1, user_input+1):
    random_table += random.choice(gen_string)

#scramble the already selected random choices
random.shuffle(random_table)

#write random table to string
for x in random_table:
    final_string += x

#print the final results
print(f"These are your scrambled words for the day {final_string}")