name1=input("What is your name? ")
name2=input("What is there name? ")

#combine both inputs
t_name = name1 + " " + name2

#convert the name to lower characters 
name_lower = t_name.lower()

#print(name_lower)

#commbine
t = t_name.count('t')
r = t_name.count('r')
u = t_name.count('u')
e = t_name.count('e')

true = t+r+u+e

l = t_name.count('l')
o = t_name.count('o')
v = t_name.count('v')
e = t_name.count('e')

love = l+o+v+e

final_score = int(str(love) + str(true))

if final_score < 10 or final_score > 90:
    print (f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >=40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
