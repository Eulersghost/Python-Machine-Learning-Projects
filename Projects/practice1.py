name1=input("What is your name? ")
name2=input("What is there name? ")

#combine both inputs
t_name = name1 + " " + name2

#convert the name to lower characters 
name_lower = t_name.lower()

#print(name_lower)

#count the strings
true_count = t_name.count('t')+t_name.count('r')+t_name.count('u')+t_name.count('e')
love_count = t_name.count('l') + t_name.count('o')+t_name.count('v')+t_name.count('e')

#combine final score
final_score = int(str(true_count) + str(love_count))

#wrap it up with if statements
if final_score < 10 or final_score > 90:
    print (f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >=40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")