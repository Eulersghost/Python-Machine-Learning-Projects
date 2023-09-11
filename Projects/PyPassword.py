#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



#-----------------------------------------------------------------------------------------------#

#This is my iteration of it, I want to use some of the tools that are provided for making projects like this 
user_password = " "
gen_password = []
random.shuffle(gen_password)

total_length = 30 
#total_passwords = 20

for x in range(1, nr_letters+1):
    gen_password.append(random.choice(letters))

for y in range(1, nr_symbols+1):
    gen_password.append(random.choice(symbols))

for z in range(1, nr_numbers+1):
    gen_password.append(random.choice(numbers))


#write a loop for each character for the final output of the user password 
for i in gen_password:
    user_password += i 


#print the passwords to the console.
final_result = ' '.join(user_password)
print(f"Your password is {final_result}")