#This is a word scrambler that I thought would be cool to write need to import the random 
import random 
import string

#fincal result displayed as a string:
total_string = " "

# variable to hold collected tables of values:
total_table = []

#define variabe to call Ascii words
generate_words = string.ascii_letters
generate_numbers = string.digits
generate_symbols = string.punctuation
generate_hex = string.hexdigits

#capture user input 
user_input = int(input("How many letters do you want to scramble? \n"))
user_input2 = int(input("How many numbers do you want to scramble? \n"))
user_input3 = int(input("How many symbols do you want to scramble? \n"))
user_input4 = int(input("How many hex digits do you want to scramble? \n"))

#write a for loop to take user input and randomize it for letters:
for char in range(1, user_input+1):
    total_table += random.choice(generate_words)
for char in range(1, user_input2+1):
    total_table += random.choice(generate_numbers)
for char in range(1, user_input3+1):
    total_table += random.choice(generate_symbols)
for char in range(1, user_input4+1):
    total_table += random.choice(generate_hex)

#Write out loop for collecting mini-tables to large table

random.shuffle(total_table)

#lastly create loop for adding characters to string:
for char in total_table:
    total_string += char



print(f"This is your word scramble for today: {total_string}")

