# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
iterate = len(names)

#We can use the variable to in the range to account for the last term in the list
random_iterate = random.randint(0, iterate-1)

#draw from the random method called on earlier
random_person = names[random_iterate]

#output result to the console
print(f"{random_person} is going to buy the meal today.")

#sample input Jason, Audajah, Jacque, Garrett, Fernando